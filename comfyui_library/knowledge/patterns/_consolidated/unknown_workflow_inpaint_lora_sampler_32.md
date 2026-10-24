---
name: unknown_workflow_inpaint_lora_sampler_32
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.896
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), InpaintModelConditioning, KSampler, LayerMask: LoadSAM2Model, LayerMask: MaskGrow, LayerMask: ObjectDetectorYOLO8, LayerMask: SAM2UltraV2, LoraLoader, PreviewAny, SaveImage, Seed (rgthree), Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/穆夏风格lora适配工作流&OneReward的手部修复功能_2028738264819048449.json, 图片生成/文生图/穆夏风格lora适配工作流&OneReward的手部修复功能（本地版）_2028865034998259714.json, 图片生成/文生图/穆夏风格lora适配工作流-flux2-klein修复手部_2017972394081652738.json, 图片生成/文生图/穆夏风格lora适配工作流-flux2-klein修复手部本地版_2028864052696457218.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/穆夏风格lora适配工作流&OneReward的手部修复功能_2028738264819048449.json、图片生成/文生图/穆夏风格lora适配工作流&OneReward的手部修复功能（本地版）_2028865034998259714.json、图片生成/文生图/穆夏风格lora适配工作流-flux2-klein修复手部_2017972394081652738.json、图片生成/文生图/穆夏风格lora适配工作流-flux2-klein修复手部本地版_2028864052696457218.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: LoadSAM2Model`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: SAM2UltraV2`
- `LoraLoader`
- `PreviewAny`
- `SaveImage`
- `Seed (rgthree)`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ColorCorrect` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `DualCLIPLoader` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `InpaintCropImproved` —— 2/4 个有
- `InpaintStitchImproved` —— 2/4 个有
- `LayerUtility: CropByMask V2` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: RestoreCropBox` —— 2/4 个有
- `MaskPreview` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `ReferenceLatent` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 18 | 6 - 30 | 4 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 50% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 18，观测区间 6 - 30，4 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
