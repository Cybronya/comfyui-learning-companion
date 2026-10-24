---
name: unknown_workflow_lora_sampler_clip_252
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.901
common_nodes: [CLIPLoader, CLIPTextEncode, GrowMaskWithBlur, ImageStitch, KSampler, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, RH_Prompter, RH_Translator, SaveImage, ShowText|pysssss, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/保持人脸高度一致，任意生图，充分发挥你的创意_1960597333257912321.json, 图片生成/图生图/按参考图生图，保持人脸高度一致_1960194814618841089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_252

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/保持人脸高度一致，任意生图，充分发挥你的创意_1960597333257912321.json、图片生成/图生图/按参考图生图，保持人脸高度一致_1960194814618841089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GrowMaskWithBlur`
- `ImageStitch`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Prompter`
- `RH_Translator`
- `SaveImage`
- `ShowText|pysssss`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
