---
name: unknown_workflow_video_lora_sampler_104
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.690647
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, GetNode, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, PrimitiveInt, SetNode, SimpleMath+, VHS_LoadVideo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/高动态双人跳舞或者动作！Animate V2！_2060564281560756226.json, 视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json, 视频生成/图生视频/Wan  图生视频 人物角色迁移 动作模仿+唱歌跳舞+舞剑   动作迁移 人物替换_2046059624503185409.json, 视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json, 视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json, 视频生成/图生视频/单人照片合成双人图高动态双人跳舞或者动作！Animate V2！_2070319838932848642.json, 视频生成/图生视频/双人_多人舞蹈_1989649967868506113.json, 视频生成/图生视频/双人舞蹈-AIGC大赏_2039884885216727041.json, 视频生成/图生视频/双人跳舞！Animate V2！B站艾橘溪_1975542884365635585.json, 视频生成/图生视频/双人跳舞！Animate V2！_2058746076395565058.json, 视频生成/图生视频/图片生成跳舞姿势模仿视频！wan2.2-Animate(长视频)动作迁移_2010268951330164737.json, 视频生成/图生视频/图生视频+双人跳舞！Animate V2！_2059808792103178241.json, 视频生成/图生视频/图生视频+双人跳舞！Animate+V2！_2064897106015510530.json, 视频生成/图生视频/超好用🔥图生视频+双人动作迁移_2062118089738776577.json, 视频生成/图生视频/高动态双人跳舞或者动作！Animate V2！_2067052913171714049.json, 视频生成/图生视频/高动态双人跳舞或者动作！Animate V2！_2072208106070822914.json, 视频生成/图生视频/高动态双人跳舞或者动作！Animate V2！_2072484558993444865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_104

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（平台全量/高动态双人跳舞或者动作！Animate V2！_2060564281560756226.json、视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json、视频生成/图生视频/Wan  图生视频 人物角色迁移 动作模仿+唱歌跳舞+舞剑   动作迁移 人物替换_2046059624503185409.json、视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json、视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveInt`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Text` —— 16/17 个有
- `VHS_VideoCombine` —— 16/17 个有
- `VHS_VideoInfo` —— 16/17 个有
- `CLIPLoader` —— 13/17 个有
- `EmptySD3LatentImage` —— 13/17 个有
- `KSampler` —— 13/17 个有
- `LoraLoaderModelOnly` —— 13/17 个有
- `Text Concatenate` —— 13/17 个有
- `Text Multiline` —— 13/17 个有
- `TextEncodeQwenImageEdit` —— 13/17 个有
- `TextEncodeQwenImageEditPlus` —— 13/17 个有
- `UNETLoader` —— 13/17 个有
- `VAEDecode` —— 13/17 个有
- `VAELoader` —— 13/17 个有
- `PreviewImage` —— 12/17 个有
- `easy cleanGpuUsed` —— 5/17 个有
- `JWInteger` —— 4/17 个有
- `ttN float` —— 4/17 个有
- `ImageFromBatch` —— 2/17 个有
- `CFGNorm` —— 1/17 个有
- `ModelSamplingAuraFlow` —— 1/17 个有
- `SaveImage` —— 1/17 个有
- `TT_img_enc_v2` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/17 个样本）：Steps较低可能导致细节不足
