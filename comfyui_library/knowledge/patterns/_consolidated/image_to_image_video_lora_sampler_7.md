---
name: image_to_image_video_lora_sampler_7
type: Image To Image
frequency: 4
level: moderate
coverage: 0.58125
common_nodes: [AILab_QwenVL, CFGNorm, CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, ImageConcanate, JWImageResize, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, PreviewImage, ProcessString, ReferenceLatent, SetNode, ShowText, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanVideoNAG]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/10s视频生成：怼脸拍摄，多动作，多动态_2005424865148633090.json, 视频生成/图生视频/10s视频生成：怼脸拍摄，多动作，多动态_2009487773425737729.json, 视频生成/图生视频/2511出图，超级动态首尾帧_2005457792624459778.json, 视频生成/图生视频/怼脸拍摄，多动作，多动态_2071866500956377090.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/10s视频生成：怼脸拍摄，多动作，多动态_2005424865148633090.json、视频生成/图生视频/10s视频生成：怼脸拍摄，多动作，多动态_2009487773425737729.json、视频生成/图生视频/2511出图，超级动态首尾帧_2005457792624459778.json、视频生成/图生视频/怼脸拍摄，多动作，多动态_2071866500956377090.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGNorm`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `JWImageResize`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PreviewImage`
- `ProcessString`
- `ReferenceLatent`
- `SetNode`
- `ShowText`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `FL_ImageListToImageBatch` —— 3/4 个有
- `ImageBatch` —— 3/4 个有
- `ImageFromBatch+` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `ImageListToBatch` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `Int` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 4 | 54% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 75%
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
