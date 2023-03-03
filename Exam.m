
%Adding top and bottom of the basin

[Basin,R] = readgeoraster('WMOBB_Basins.tif');

Top = int16(NaN(13,720));
Bottom = int16(NaN(68,720));
Basin_new = [Top; Basin; Bottom];
Basin_new_1 = double(Basin_new);


%Grace procesing - rotating,shifting, missing month, interpolation

Grace = 'GRCTellus.JPL.200204_202207.GLO.RL06M.MSCNv02CRI.nc';
Grace_lwe = ncread(Grace,'lwe_thickness');
ncdisp(Grace)


Rot_lwe = rot90(Grace_lwe);
Grace_full = Rot_lwe(:,:,211);
left_TT_lwe= Rot_lwe(:,1:360,211);
right_TT_lwe= Rot_lwe(:,361:720,211);
Grace_FN = [right_TT_lwe left_TT_lwe];


datetime.setDefaultFormats('defaultdate','yyyy-MM-dd');  
Date = datetime(2002,04,16):calmonths(1):datetime(2022,07,16); 
Date.Format = 'yyyy-MM'; 
Date = Date';

MM = ["2002-06";"2002-07";"2003-06";"2011-01";"2011-06";"2012-05";"2012-10";"2013-03";"2013-08";"2013-09";"2014-02";"2014-07";"2014-12";"2015-06";"2015-10";"2015-11";"2016-04";"2016-09";"2016-10";"2017-02";"2017-07";"2017-08";"2017-09";"2017-10";"2017-11";"2017-12";"2018-01";"2018-02";"2018-03";"2018-04";"2018-05";"2018-08";"2018-09"];

for i = 1:size(MM)
    MM(i) = strcat(MM(i),"-16");
    MM_DateTime(i) = datetime(MM(i),'InputFormat','yyyy-MM-dd');
end
MM_DateTime.Format = 'yyyy-MM';
MM_DateTime = MM_DateTime';

S = size(Date);
M = size(MM_DateTime);
count = 0;
j = 1;

for i = 1:S(1)
    lwe_stack(:,:,i) = Rot_lwe(:,:,j);
    if( (Date(i) == MM_DateTime(count+1)) && (count<=M(1)-1) )  
        lwe_stack(:,:,i) = NaN(360,720);
        if count >= M(1)-1
            count = count^1;
        else
            count = count + 1; 
        end
        j = j - 1;
    end
    j = j + 1;
end


%interpolation
for i =1:360
    for j=1:720
        Grace_fill(i,j,:)=fillmissing(lwe_stack(i,j,:),"previous");  
    end
end

%Masking

Basin_Mask = NaN(360,720);

for i = 1:360
    for j = 1:720
        if(Basin_new_1(i,j) == 148 )
             Basin_Mask(i,j) = 1;
        end
    end
end

for k = 1:244
    Grace_masked(:,:,k) = Grace_fill(:,:,k).* Basin_Mask;      
end




imagesc(Grace_masked(:,:,200))

plot(squeeze(Grace_masked(123,530,:)))


% slpall=zeros(360,720);
% 
% for i = 1 : 360
%     for j = 1 : 720
%         Slope = polyfit (Grace_masked(i,j,:),1);
%         slpall(i,j)=Slope(:,2);
%      end
%  end

