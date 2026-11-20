---
name: unknown_workflow_inpaint_lora_sampler_40
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.969667
common_nodes: [CLIPLoader, CLIPTextEncode, ImageConcanate, ImagePadKJ, InpaintModelConditioning, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingSD3, PDIMAGE_LongerSize, PreviewImage, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226.json, 图片生成/图生图/Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282.json, 图片生成/图生图/啊癫 wan2.2修手_1954124114648809474.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Wan2.1 Vace图像局部修复图生图（最强修手）V3_1944821353327284226.json、图片生成/图生图/Wan2.2 Vace图像局部修复图生图（最强修手）V1_1950509812612321282.json、图片生成/图生图/啊癫 wan2.2修手_1954124114648809474.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcanate`
- `ImagePadKJ`
- `InpaintModelConditioning`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_TextToStringAndSeed` —— 2/3 个有
- `PMRF` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 3 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.25 | 0.25 - 0.25 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.25，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
