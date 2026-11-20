---
name: unknown_workflow_inpaint_sampler_unet_2
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.918222
common_nodes: [DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】Flux fill OneReward 无痕局部重绘工作流_1970072675894915074.json, 图片生成/图生图/【阡陌】Flux fill OneReward 无痕扩图工作流_1970470713633218562.json, 图片生成/图生图/局部重绘移除(河南ai之神)_1931906923506151425.json, 图片生成/图生图/擦除，去除，物体移除，无痕消除， Onereward优化版_1941296102585036801.json, 图片生成/图生图/无痕消除，人物移除 物体移除 Removal 升级版_1978318239086305281.json, 图片生成/图生图/涂抹擦除工具OneReward-Fill最强擦除 工具【支持超大面积擦除】_2104707997896372226.json, 图片生成/文生图/OneReward-Fill重绘_1985864428728066050.json, 图片生成/文生图/去水印_1989239057773367297.json, 视频生成/图生视频/OneReward-Fill-最强局部重绘-遮罩涂抹模式_1981616130160762881.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet_2

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/【阡陌】Flux fill OneReward 无痕局部重绘工作流_1970072675894915074.json、图片生成/图生图/【阡陌】Flux fill OneReward 无痕扩图工作流_1970470713633218562.json、图片生成/图生图/局部重绘移除(河南ai之神)_1931906923506151425.json、图片生成/图生图/擦除，去除，物体移除，无痕消除， Onereward优化版_1941296102585036801.json、图片生成/图生图/无痕消除，人物移除 物体移除 Removal 升级版_1978318239086305281.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 8/9 个有
- `Image Comparer (rgthree)` —— 8/9 个有
- `CLIPTextEncode` —— 7/9 个有
- `LoraLoaderModelOnly` —— 7/9 个有
- `GrowMaskWithBlur` —— 6/9 个有
- `ImpactInt` —— 6/9 个有
- `Mask Fill Holes` —— 6/9 个有
- `LayerMask: MaskGrow` —— 5/9 个有
- `ColorCorrect` —— 4/9 个有
- `LayerUtility: CropByMask V2` —— 4/9 个有
- `LayerUtility: RestoreCropBox` —— 4/9 个有
- `ToBinaryMask` —— 4/9 个有
- `easy ifElse` —— 4/9 个有
- `easy boolean` —— 3/9 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 2/9 个有
- `EasyCache` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `DeepTranslatorTextNode` —— 1/9 个有
- `ImagePadForOutpaintMasked` —— 1/9 个有
- `MaskPreview` —— 1/9 个有
- `PrimitiveBoolean` —— 1/9 个有
- `RH_Translator` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 26 | 8 - 40 | 9 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 56% |
| 调度器 | simple | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 26，观测区间 8 - 40，9 个样本，取值分散，一致性仅 50%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
