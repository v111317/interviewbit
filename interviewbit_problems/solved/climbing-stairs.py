#https://www.interviewbit.com/problems/climbing-stairs/

class Solution:    
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        costArr = []
        costArr.append(A[0])
        costArr.append(A[1]+A[0])
        
        for i in range(2, len(A)):
            costArr.append(A[i] + min(costArr[i-1], costArr[i-2]))
        return costArr[len(A)-1]
        
sol1 = Solution()
print(sol1.solve([1,2,1,3]))
print(sol1.solve([1,2,3,4]))
#list1 = "100000 1316 7557 4587 5328 2190 471 6789 6793 9347 3836 5195 8310 346 535 5298 6712 77 3835 669 4175 6868 5890 9305 8462 5270 920 6540 4161 7012 9104 7622 2625 475 7361 3283 6327 7565 9911 3654 2471 9826 7227 7534 6516 727 6317 8848 2728 4365 7665 4778 2378 2750 3593 1666 4866 8977 9093 606 9047 5046 5163 3191 9867 4940 2662 908 9478 738 5008 3842 2771 9139 5298 4645 9410 501 7616 7703 8279 1254 159 6885 8683 6296 7363 7255 9995 8886 2332 3064 3511 5133 5912 8460 4121 8416 2694 4154 5374 4680 2873 1784 1538 5717 8025 331 5345 4985 9554 7483 5546 8908 6249 8421 1598 2128 7148 1305 910 2746 30 4143 269 7099 9379 2400 1809 3176 8870 6521 1504 6814 3859 3878 4998 1476 5872 8456 5902 9555 5562 1482 9834 4088 1419 5649 2522 4886 4641 9611 1261 1998 3193 6293 1268 6513 6217 8031 2479 4765 3894 2033 284 9017 4265 1421 9475 4104 1312 8857 922 1622 711 3654 2531 1352 7832 4554 3496 4524 8090 9317 6517 2153 6796 9090 2502 8609 4713 5060 6004 8176 7559 4623 9514 6328 4394 8247 6890 7023 9872 9545 8513 2894 5375 5145 1035 4141 5768 8766 4401 7298 8693 7157 8008 7066 7418 191 8861 5250 4634 652 7135 4890 6677 6821 1996 9167 8659 8901 5440 1392 4504 9894 2156 4461 3158 5147 8816 4398 4676 8067 3652 2116 9992 1537 6305 6164 6 9 7734 7274 3192 4178 6825 6806 2053 8365 7090 8288 946 818 7641 6296 2139 2136 811 3889 9522 9476 3899 2693 6922 2841 7769 7839 4225 2822 1940 114 1919 9833 2441 8198 1365 3982 6011 1769 8284 1578 9880 2572 2336 1017 2195 6348 6961 7948 6963 7530 6696 6335 565 5983 2271 3188 6999 1175 7626 5262 5540 5880 3297 7030 1431 1617 4854 8603 8133 5569 7390 3161 1354 5286 3108 5882 5181 4309 2589 3703 3931 4469 4759 3879 2793 783 3698 2540 6718 6763 5140 7287 7208 9448 4607 9402 3216 4605 5172 6614 4019 6057 9866 1504 6701 3439 5418 5229 8293 150 2743 6430 5462 9179 2667 9701 2468 8440 6941 4558 8172 221 1608 7070 7079 4367 5825 7518 9916 6957 2796 7539 1712 43 4957 800 1631 9034 7830 7467 4365 64 5848 5185 669 5441 3898 2159 3858 6269 6591 7094 5387 2803 8160 3720 6862 3102 94 1038 5210 7759 2207 553 707 1603 7238 2971 507 4779 4572 5200 4465 1504 2860 8337 6957 5778 6812 3312 575 9869 5424 17 8562 294 3776 4897 5762 7390 6794 5363 356 1226 9734 1883 3514 6142 6077 1260 5529 9541 3570 8382 9743 2591 2516 4244 8131 8980 2446 7607 6949 4519 2637 6656 1166 2096 1137 5470 61 1760 5994 4320 826 6875 3754 8363 1237 9734 297 804 4943 7695 9341 2502 3597 7692 5000 7493 6720 6817 7568 364 2306 2217 5627 6527 6167 3715 2249 2337 6531 1660 7442 1598 477 6620 1250 9492 4842 6211 9141 180 5936 7219 4966 537 4417 5192 7720 654 4428 9772 4678 3291 4460 7433 2054 1714 3726 9398 9649 2550 704 1239 5264 1601 5178 1052 8416 3686 4239 3273 7136 5768 8719 7583 8366 6998 3891 9353 6057 3621 5396 4551 4017 2405 831 4216 4724 2898 1050 2164 8021 5275 6689 8637 2438 7116 2637 3829 811 4598 2329 7954 4914 33 2662 6647 4252 1869 9635 1341 7959 9461 1712 6061 639 3475 2925 5097 8259 8344 7265 3295 8021 6318 454 415 1534 7671 618 5194 9292 2206 2046 890 6997 7065 4947 2618 7116 3784 2007 2327 4361 4695 8612 9773 4446 343 5238 317 7532 5916 8229 3296 2321 5366 4307 4036 9874 9670 8506 8676 3117 1484 9977 6396 4681 9320 6908 8155 5416 5729 1593 9453 8214 1555 411 3437 1101 966 5188 225 5615 8569 5170 6746 7372 6985 228 1920 6710 3459 663 1408 9212 2217 3802 5861 1674 264 6912 7624 7137 774 5899 9256 9297 4305 5060 8313 9193 6017 7239 5194 4909 1615 9762 5744 2733 5315 6986 6671 975 5488 6108 6680 4952 5716 5889 4414 1513 5023 7314 317 517 5221 3207 351 2452 1072 3830 5519 5972 6112 9353 7721 5132 4867 6502 6970 4076 4869 4798 7105 5342 2767 6056 2802 7034 5305 9383 2355 4135 5975 7831 9203 6815 8212 5275 2303 1437 8996 2515 6516 49 9360 2754 8588 2790 9525 5069 1230 4165 7025 4365 1078 7662 999 4413 3446 2971 7577 3386 3308 557 5732 4853 2025 1145 9744 8647 4919 3674 8050 1623 1596 578 1493 4682 3807 8838 4242 4123 6513 3084 602 8145 8977 9195 9013 7701 1708 5725 315 8033 5223 8617 2772 8695 5869 3892 8119 5257 9399 4201 5799 7492 8808 3381 1896 7432 7190 8792 729 7102 8791 3594 899 1611 4168 965 6747 5627 8131 8782 7694 6353 8966 8785 4865 1131 3775 3827 6876 1218 769 1434 4777 7086 2381 3910 9759 6288 6812 9087 3625 8593 7943 4289 736 4987 4839 4508 4997 7408 9329 3002 1462 1101 804 9725 4082 2385 9632 8335 1981 1295 1964 3392 5757 4403 5857 4329 3683 3824 6002 4295 1488 6702 9955 6981 4028 8493 8196 7934 3743 97 4798 6391 6465 6449 7991 3774 3577 3896 3344 6936 1449 2916 6669 8544 3147 1442 6023 56 9209 3820 5166 3445 2642 2911 8337 1244 6347 487 4581 3769 1559 7559 6660 116 7949 5610 2887 4156 3207 5146 7192 8421 2319 4651 3734 501 739 2025 5662 8316 4226 8396 2931 1812 3576 9342 5895 3691 4631 6279 9445 4058 505 4449 5960 7484 8642 1311 1046 6654 8334 5813 6586 9821 190 9215 1947 9678 5231 2788 7198 5905 8371 8347 6599 7305 6431 3496 5349 6642 3235 8692 4424 9180 2767 9518 1173 4161 8364 9626 3330 5262 5360 8182 9299 6629 2433 9415 5968 1261 2470 8868 1962 1630 8360 6025 6233 8387 6717 3916 8713 6674 1157 1 6761 6288 4546 5744 323 3514 8551 3709 6615 5765 600 7445 2795 4427 1765 919 8973 9925 5942 331 6910 4873 5694 8958 4346 6886 2032 4818 2725 9472 2444 9533 4770 1271 9615 8572 2175 71 7825 504 9601 6414 5735 1371 1291 8247 5019 6559 5051 5265 1184 9031 6690 2776 3868 3915 8311 2431 1235 7284 6481 2013 8487 226 1056 1880 3610 7797 7193 6664 5810 3512 1572 2921 1692 2237 6714 4048 8866 5794 3419 4373 6997 8343 7920 8491 2823 2647 1700 5336 732 9988 7502 1223 1646 4252 7733 2136 4340 331 9294 1061 2663 4821 7928 2576 2140 2825 3807 2082 9286 7641 6166 5759 3564 9079 1980 1142 7912 6982 183 7480 1146 8950 6547 3459 3825 2151 3313 178 9144 7855 3935 7300 8316 8778 1297 3435 9421 3622 3521 807 5719 7764 8443 4933 8174 6428 4354 3524 3492 2816 9192 6262 7446 1576 7765 2520 6121 8547 3147 6085 1260 3737 1333 2619 1261 2029 7506 710 4590 9633 2347 1976 6840 814 8543 1526 1202 8092 9442 456 603 8298 1412 8012 2275 3993 5992 6553 538 9864 8124 4136 319 1081 9745 8672 6711 8344 2383 7170 5898 2226 2278 16 4479 4098 9331 225 5135 3766 8596 7939 6095 3319 6241 6539 6444 2592 261 9871 2078 6424 5604 3770 1207 4492 1378 5859 5427 4837 8867 816 3626 1009 2993 8417 9131 8280 9704 8133 7979 8398 4488 6421 6940 8158 4683 1937 4016 9307 4673 3785 5176 2278 8993 9859 1370 4585 6892 2791 4093 7400 313 3040 1927 8132 2749 7178 4087 7851 7223 5771 6330 7986 3 6278 3465 4719 4923 5297 3186 8580 1381 3992 3870 8465 562 4569 7656 2925 9620 9991 7417 3498 7966 1991 6008 5429 2517 2017 5757 5138 7478 6081 9897 7985 5548 1467 1071 5238 2464 5717 3344 6788 694 8447 8763 3321 1455 7441 6619 4028 5851 5555 4942 6146 9249 6140 2564 397 6208 3435 242 1714 6108 4239 5685 7304 3740 3657 3763 867 5832 4182 1109 3253 6852 5640 8719 5319 9746 603 4754 1102 9922 5496 6988 1273 4750 594 4452 9180 4396 8586 9972 5494 1243 8464 1903 6644 6563 9732 4577 1594 1392 2834 9730 5980 8523 629 9257 9494 4667 2823 4603 4309 8662 1987 3848 7592 8143 6728 7216 6834 3140 1685 6881 9210 1658 39 1764 1782 1981 6683 6745 5175 3235 4670 3209 937 8705 4452 1478 6521 9420 8824 6610 2040 1704 161 1655 1091 3612 5612 9639 2455 239 301 8862 8864 9133 5475 1726 4871 8145 9367 5831 5490 4718 7534 3324 1725 5130 3805 8282 9671 48 3014 4546 8905 8436 2504 7340 8396 4230 7085 4059 5264 5256 916 4037 7822 2648 3079 1850 7567 6207 6454 3274 1543 1844 4552 5332 1625 9258 4091 312 1673 5651 9855 1403 3336 3092 3544 1629 3222 3796 6414 6024 377 3352 783 5441 4912 2879 2528 4394 6587 3256 17 9727 1009 3184 9556 3493 1655 9855 1165 419 9610 7853 2204 1015 2546 4376 2431 2826 5493 8824 8517 6705 5577 7579 9020 8534 7597 2340 9983 2613 3751 2996 7456 9919 7664 4287 6417 4639 1025 1819 8634 5034 9310 8981 2912 6292 9755 5441 8307 549 1897 9753 7653 8699 324 5185 3755 9697 1932 2286 5970 8966 5495 848 7770 7711 7084 520 8836 717 9947 2700 4998 6874 7485 9447 6898 9118 1713 8154 2829 4819 9109 7032 3994 1685 9025 2101 5484 3728 2632 8068 2359 6590 3357 5222 4529 6069 6672 218 8193 3774 5418 9698 7463 7933 7588 4533 4068 2443 7023 2139 6612 4071 2764 3432 3015 6885 9543 7782 9024 217 9743 538 4100 1636 7961 116 6021 9215 1100 5451 731 5566 3834 4815 3910 4087 5592 9411 6991 5897 112 2828 3874 7458 5657 5544 2686 1172 1617 3544 8084 2658 1917 4145 6482 5297 729 4700 3790 989 4933 1329 2163 4383 3532 9939 8922 3500 4392 8017 9822 3013 5767 5520 1433 5066 4999 7297 826 2171 1730 3853 3747 2644 1647 8566 2455 8934 7912 9642 2508 2841 5499 7189 5153 4865 3519 8585 4123 205 9157 9596 5687 9979 4006 5877 8064 4083 435 5455 1301 5748 9693 6814 2073 5639 8307 2929 3061 9780 9850 5838 3329 5216 824 8078 6817 5948 2042 2005 1640 2808 1975 7931 8719 7893 908 1601 2471 7615 5171 3918 8680 3327 5968 7803 9868 9544 8229 7771 6865 8420 6280 7684 3967 5853 4201 8017 4778 6908 8137 5510 2948 5870 4744 8987 4293 2600 4641 1 6581 919 5624 6791 6677 7453 6525 9820 2797 7828 52 869 592 9268 2147 7814 2537 2866 7382 2959 4732 9100 9231 8918 2507 7525 6840 4682 4740 2088 5064 8978 8351 9588 9732 9185 1488 2629 3965 7715 7707 7758 4545 4187 6364 6471 7421 8295 2722 7803 1805 1200 7878 9919 773 4250 8412 6336 9449 4304 9460 7986 3772 2468 8288 417 2287 941 8615 435 9547 8243 8691 5120 7502 9984 4175 2117 4038 1090 3621 969 2040 3871 8236 8993 9659 8171 4169 8175 7250 4586 4152 5928 6034 6676 9875 7391 43 6255 1302 8961 6779 3284 2369 4515 6808 2589 1460 7039 5988 6910 738 8797 2030 2168 7326 7857 9583 7155 7405 1953 2155 205 8392 7609 2187 4202 2708 6769 8359 505 6229 6337 4578 1096 7253 176 4129 5382 1023 6404 4358 279 2425 3300 6319 3758 5447 7689 790 7628 483 1846 4704 8385 3385 3684 8538 7868 2786 8153 7034 8979 8704 4129 1820 5545 5310 3510 7253 9720 2354 1409 2378 8016 8224 4011 8679 6024 387 7552 4878 9787 3553 7299 1651 8789 3104 6776 1504 2879 9068 222 5918 9446 8294 5682 2114 304 5822 6417 1551 683 3076 5744 3687 2101 350 7570 653 2754 7706 3743 3029 3545 9673 6223 6979 3466 1545 5161 5655 6965 6890 8077 4589 7362 1618 3279 125 4407 8055 9331 5635 5671 5757 9878 7285 1112 5109 4445 4748 5450 5852 1485 7257 5255 3452 5878 330 90...
#207200535