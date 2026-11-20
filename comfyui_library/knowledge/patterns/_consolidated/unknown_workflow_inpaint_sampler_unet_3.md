---
name: unknown_workflow_inpaint_sampler_unet_3
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.905273
common_nodes: [ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【阡陌】Flux fill OneReward 无痕局部重绘工作流_1970072675894915074.json, 图片生成/图生图/【阡陌】Flux fill OneReward 无痕扩图工作流_1970470713633218562.json, 图片生成/图生图/擦除，去除，物体移除，无痕消除， Onereward优化版_1941296102585036801.json, 图片生成/图生图/无痕消除，人物移除 物体移除 Removal 升级版_1978318239086305281.json, 图片生成/图生图/涂抹擦除工具OneReward-Fill最强擦除 工具【支持超大面积擦除】_2104707997896372226.json, 图片生成/文生图/OneReward-Fill重绘_1985864428728066050.json, 图片生成/文生图/去水印_1989239057773367297.json, 平台全量/OneReward-Fill最强擦除【支持超大面积擦除】_1978691503067435010.json, 平台全量/【万物迁移】OneReward-Fill最强重绘【高清出图】_1980137233330114562.json, 平台全量/局部重绘_1991696291300323330.json, 视频生成/图生视频/OneReward-Fill-最强局部重绘-遮罩涂抹模式_1981616130160762881.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/【阡陌】Flux fill OneReward 无痕局部重绘工作流_1970072675894915074.json、图片生成/图生图/【阡陌】Flux fill OneReward 无痕扩图工作流_1970470713633218562.json、图片生成/图生图/擦除，去除，物体移除，无痕消除， Onereward优化版_1941296102585036801.json、图片生成/图生图/无痕消除，人物移除 物体移除 Removal 升级版_1978318239086305281.json、图片生成/图生图/涂抹擦除工具OneReward-Fill最强擦除 工具【支持超大面积擦除】_2104707997896372226.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
- `ConditioningZeroOut`
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
- `Image Comparer (rgthree)` —— 10/11 个有
- `CLIPTextEncode` —— 9/11 个有
- `GrowMaskWithBlur` —— 9/11 个有
- `ImpactInt` —— 9/11 个有
- `LayerMask: MaskGrow` —— 8/11 个有
- `Mask Fill Holes` —— 8/11 个有
- `ColorCorrect` —— 7/11 个有
- `LayerUtility: CropByMask V2` —— 7/11 个有
- `LayerUtility: RestoreCropBox` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `ToBinaryMask` —— 7/11 个有
- `easy ifElse` —— 7/11 个有
- `easy boolean` —— 6/11 个有
- `CR Text` —— 3/11 个有
- `DeepTranslatorTextNode` —— 3/11 个有
- `ArgosTranslateCLIPTextEncodeNode` —— 2/11 个有
- `EasyCache` —— 2/11 个有
- `ImagePadForOutpaintMasked` —— 1/11 个有
- `MaskPreview` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `PrimitiveBoolean` —— 1/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 40 | 11 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 64% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 40，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 64%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
