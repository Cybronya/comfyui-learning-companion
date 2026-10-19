---
name: unknown_workflow_video_sampler_vae_4
type: Unknown Workflow
frequency: 36
level: moderate
coverage: 0.939889
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [Primitive integer [Crystools], Text Multiline]
members: [图片生成/文生图/1936223818082062337.json, 视频生成/图生视频/1936223818082062337.json, 视频生成/图生视频/1934999093192105986.json, 视频生成/图生视频/1929947388339765250.json, 视频生成/图生视频/1927584684270850049.json, 视频生成/图生视频/1949398182790365185.json, 视频生成/图生视频/1941647575110074369.json, 视频生成/图生视频/1942759645448744961.json, 视频生成/图生视频/1945356910293917698.json, 视频生成/图生视频/2081288501450076161.json, 视频生成/图生视频/2067619430019977218.json, 视频生成/图生视频/2067873046999945218.json, 视频生成/图生视频/MAGREF-吻屏图生视频_2104531594294943746.json, 视频生成/图生视频/MAGREF-吻屏图生视频_2104542133922385921.json, 视频生成/图生视频/2026931887591133185.json, 视频生成/图生视频/2046763253136625665.json, 视频生成/图生视频/1958913367148802050.json, 视频生成/图生视频/1960985740777852930.json, 视频生成/图生视频/1946494882895523842.json, 视频生成/图生视频/1946072429141651458.json, 视频生成/图生视频/1933737212456390657.json, 视频生成/图生视频/1934536025144238081.json, 视频生成/图生视频/1948954040869761026.json, 视频生成/图生视频/1944601523588354050.json, 视频生成/图生视频/1944648210231250946.json, 视频生成/图生视频/1961656258828943362.json, 视频生成/图生视频/2062016628551933953.json, 视频生成/图生视频/2062080584259817473.json, 视频生成/图生视频/2072700454361976834.json, 视频生成/图生视频/2072700639905406978.json, 视频生成/图生视频/1946542261884870657.json, 视频生成/图生视频/1945368042832371714.json, 视频生成/图生视频/1945027007760752641.json, 视频生成/图生视频/1943493844422062081.json, 视频生成/图生视频/1977981192005976065.json, 视频生成/图生视频/1946134674865614850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_4

> 由 `engine/knowledge_consolidation` 从 36 个 workflow 归纳得出（图片生成/文生图/1936223818082062337.json、视频生成/图生视频/1936223818082062337.json、视频生成/图生视频/1934999093192105986.json、视频生成/图生视频/1929947388339765250.json、视频生成/图生视频/1927584684270850049.json…）

- **类型**：Unknown Workflow
- **样本数**：36
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 36 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 35/36 个有
- `WanVideoLoraSelect` —— 34/36 个有
- `JWInteger` —— 20/36 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/36 个有
- `WanVideoTeaCache` —— 20/36 个有
- `WanVideoExperimentalArgs` —— 18/36 个有
- `WanVideoSLG` —— 18/36 个有
- `WanVideoTorchCompileSettings` —— 18/36 个有
- `LayerUtility: PurgeVRAM V2` —— 17/36 个有
- `Primitive integer [Crystools]` —— 16/36 个有
- `ImageResizeKJ` —— 14/36 个有
- `WanVideoFreeInitArgs` —— 14/36 个有
- `WanVideoVRAMManagement` —— 14/36 个有
- `WanVideoVACEModelSelect` —— 13/36 个有
- `ImageResize+` —— 4/36 个有
- `MathExpression|pysssss` —— 4/36 个有
- `ImageResizeKJv2` —— 3/36 个有
- `ImageConcanate` —— 2/36 个有
- `Float` —— 1/36 个有
- `RH_Translator` —— 1/36 个有
- `WanVideoEasyCache` —— 1/36 个有
- `WanVideoLoraSelectMulti` —— 1/36 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Primitive integer [Crystools]、Text Multiline
