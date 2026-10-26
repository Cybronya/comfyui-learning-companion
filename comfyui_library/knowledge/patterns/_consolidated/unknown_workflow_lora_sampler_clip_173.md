---
name: unknown_workflow_lora_sampler_clip_173
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.919
common_nodes: [CLIPLoader, CLIPTextEncode, GrowMaskWithBlur, KSampler, LayerMask: MaskPreview, LayerMask: SegmentAnythingUltra V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, ShowText|pysssss, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/33realisticfaceswap_2049744111430844417.json, 图片生成/图生图/保持人脸高度一致，任意生图，充分发挥你的创意_1960597333257912321.json, 图片生成/图生图/按参考图生图，保持人脸高度一致_1960194814618841089.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_173

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/33realisticfaceswap_2049744111430844417.json、图片生成/图生图/保持人脸高度一致，任意生图，充分发挥你的创意_1960597333257912321.json、图片生成/图生图/按参考图生图，保持人脸高度一致_1960194814618841089.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GrowMaskWithBlur`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `ShowText|pysssss`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Prompter` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
