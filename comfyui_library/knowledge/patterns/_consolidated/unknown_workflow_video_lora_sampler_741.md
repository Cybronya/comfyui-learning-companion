---
name: unknown_workflow_video_lora_sampler_741
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.781667
common_nodes: [CLIPLoader, CLIPTextEncode, Compare, GetImageSize, GetNode, ImageResize+, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RHHiddenNodes, SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_Unbatch, VHS_VideoCombine, WanFirstMiddleLastFrameToVideo, easy batchAnything, easy cleanGpuUsed, easy ifElse, easy imageListToImageBatch, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/【九镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1989325404936826881.json, 视频生成/图生视频/【五镜联动·一键制作】分镜_关键帧联动_1989305168229486593.json, 视频生成/图生视频/【五镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1988497511591665666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_741

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/【九镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1989325404936826881.json、视频生成/图生视频/【五镜联动·一键制作】分镜_关键帧联动_1989305168229486593.json、视频生成/图生视频/【五镜联动·超燃短片一键制作】全能图片pro 故事分镜V2-Wan2.2 FMLM 关键帧联动_1988497511591665666.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Compare`
- `GetImageSize`
- `GetNode`
- `ImageResize+`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RHHiddenNodes`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_Unbatch`
- `VHS_VideoCombine`
- `WanFirstMiddleLastFrameToVideo`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageListToImageBatch`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `RH_Nano_Banana2_Image2Image` —— 2/3 个有
- `Int` —— 1/3 个有
- `RH_Nano_Banana_Image2Image` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
