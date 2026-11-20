---
name: unknown_workflow_video_lora_sampler_456
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6208
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, GetNode, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/文生图/video_wan2_2_14B_t2i_halftone_1990239408819499010.json, 图片生成/文生图/video_wan2_2_数字人工作流1-生成_1953391990853521409.json, 图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json, 图片生成/文生图/wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385.json, 图片生成/文生图/wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_456

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/video_wan2_2_14B_t2i_halftone_1990239408819499010.json、图片生成/文生图/video_wan2_2_数字人工作流1-生成_1953391990853521409.json、图片生成/文生图/wan2.2 lora最好用的林黛玉妹妹工作流和模型-可生成该人物任意写实风-可用于抖音快手等自媒体_1989283451264225282.json、图片生成/文生图/wan2.2文生图和视频古典美女lora工作流-美女一致性和让wan2.2人物可控性更好_1970462683160080385.json、图片生成/文生图/wan2.2文生图和视频美女lora工作流-美女保持完美一致性_1961428825634750466.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `GetNode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 4/5 个有
- `VHS_VideoCombine` —— 4/5 个有
- `JWStringMultiline` —— 3/5 个有
- `JoinStringMulti` —— 3/5 个有
- `String` —— 3/5 个有
- `PreviewImage` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `VAEUtils_CustomVAELoader` —— 1/5 个有
- `VAEUtils_VAEDecodeTiled` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 2.5 | 1 - 2.5 | 5 | 61% |
| 调度器 | ddim | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.5，观测区间 1 - 2.5，5 个样本
- 调度器 最常用 ddim，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
