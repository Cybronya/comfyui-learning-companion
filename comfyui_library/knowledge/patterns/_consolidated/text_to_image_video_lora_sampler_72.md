---
name: text_to_image_video_lora_sampler_72
type: Text To Image
frequency: 11
level: strong
coverage: 0.751727
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, ColorMatch, EmptyImage, EmptyLatentImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageResizeKJ, ImpactSwitch, JjkText, KSampler, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, Primitive integer [Crystools], RHHiddenNodes, SetNode, SimpleMath+, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/玩偶特化8秒版v2 动漫角色跳舞视频一键生成_2094811901338411010.json, 视频生成/图生视频/V1版本 150帧跳舞动作迁移 直出1920P高清画质视频_2094821599244546050.json, 视频生成/图生视频/V1版本直出1920P高清动作迁移跳舞150帧_2087325234281144321.json, 视频生成/图生视频/V1版本直出1920P高清动作迁移跳舞150帧_2087471552114806786.json, 视频生成/图生视频/V1跳舞动作迁移｜150帧直出1920P高清图生视频_2092188304195284994.json, 视频生成/图生视频/V2版本直出1920高清超高拟态舞蹈160帧_2087323889797001217.json, 视频生成/图生视频/V2版本直出1920高清超高拟态舞蹈160帧_2087470174856368129.json, 视频生成/图生视频/V2超高拟态舞蹈｜160帧直出1920高清动作迁移_2092184846041960450.json, 视频生成/图生视频/平行世界的我起号专用动作迁移图生视频_2087313287083020289.json, 视频生成/图生视频/平行世界的我风格转换｜动漫手办乐高多风格视频生成_2097806857049042945.json, 视频生成/图生视频/平行世界的我｜起号专用动作迁移图生视频一键生成_2092147311823638530.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/玩偶特化8秒版v2 动漫角色跳舞视频一键生成_2094811901338411010.json、视频生成/图生视频/V1版本 150帧跳舞动作迁移 直出1920P高清画质视频_2094821599244546050.json、视频生成/图生视频/V1版本直出1920P高清动作迁移跳舞150帧_2087325234281144321.json、视频生成/图生视频/V1版本直出1920P高清动作迁移跳舞150帧_2087471552114806786.json、视频生成/图生视频/V1跳舞动作迁移｜150帧直出1920P高清图生视频_2092188304195284994.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 11 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `EmptyImage`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `ImpactSwitch`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `SetNode`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 10/11 个有
- `PreviewImage` —— 10/11 个有
- `RH_Captioner` —— 10/11 个有
- `ShowText|pysssss` —— 7/11 个有
- `WanVideoBlockSwap` —— 4/11 个有
- `WanVideoLoraSelect` —— 4/11 个有
- `WanVideoModelLoader` —— 4/11 个有
- `WanVideoTorchCompileSettings` —— 4/11 个有
- `WanVideoVACEModelSelect` —— 4/11 个有
- `ConditioningZeroOut` —— 3/11 个有
- `DualCLIPLoader` —— 3/11 个有
- `FluxGuidance` —— 3/11 个有
- `FluxKontextImageScale` —— 3/11 个有
- `ImageBlend` —— 3/11 个有
- `NunchakuFluxDiTLoader` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `ReferenceLatent` —— 3/11 个有
- `SaveImage` —— 3/11 个有
- `Seed_` —— 3/11 个有
- `Text` —— 3/11 个有
- `VAEEncode` —— 3/11 个有
- `easy imageConcat` —— 3/11 个有
- `easy seed` —— 3/11 个有
- `ImageResize+` —— 1/11 个有
- `RH_LLMAPI_NODE` —— 1/11 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
