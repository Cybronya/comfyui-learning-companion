---
name: unknown_workflow_video_lora_sampler_893
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9485
common_nodes: [CLIPVisionLoader, DrawViTPose, Float, GetImageSizeAndCount, ImageBatch, ImageFromBatch, ImageResizeKJv2, Int, LoadImage, MemoryCleaner, OnnxDetectionModelLoader, PoseAndFaceDetection, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移测试_2104214457558855681.json, 视频生成/图生视频/灵活分段生视频 4段变装+动作迁移+服装替换+人脸替换+ 灵活分段版_2089231514004447234.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_893

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/动作迁移测试_2104214457558855681.json、视频生成/图生视频/灵活分段生视频 4段变装+动作迁移+服装替换+人脸替换+ 灵活分段版_2089231514004447234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `Float`
- `GetImageSizeAndCount`
- `ImageBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MemoryCleaner`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `WujiCleaner` —— 1/2 个有
- `WujiUpscaler` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
