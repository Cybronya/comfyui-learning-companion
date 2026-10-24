---
name: unknown_workflow_lora_sampler_unet_76
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.812
common_nodes: [ConditioningZeroOut, DiptychCreate, DualCLIPLoader, FluxGuidance, ICEFConditioning, InContextEditInstruction, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/ICEdit-MoE 图像编辑 超强图像编辑处理_1921801961237315586.json, 图片生成/图生图/IcEdit多条件图像编辑工作流（支持蒙版）基础V1_1920532699742666753.json, 图片生成/图生图/flux-ICEdit-超强一致性_1922121608931000322.json, 图片生成/图生图/【💫书墨】ICEdit-normal-lora官方实现_1920767853685833729.json, 图片生成/图生图/图像编辑(图加提示词即可实现图像编辑，无需mask)_1930500823778803713.json, 图片生成/图生图/木乙创设—IcEdit加速优化官方工作流_1921407429425184769.json, 图片生成/文生图/图像编辑无需重复抽卡_1932629301877424130.json, 图片生成/文生图/真ICEdit官方版一致性图像编辑无需重复抽卡_1920517668280143874.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_76

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/ICEdit-MoE 图像编辑 超强图像编辑处理_1921801961237315586.json、图片生成/图生图/IcEdit多条件图像编辑工作流（支持蒙版）基础V1_1920532699742666753.json、图片生成/图生图/flux-ICEdit-超强一致性_1922121608931000322.json、图片生成/图生图/【💫书墨】ICEdit-normal-lora官方实现_1920767853685833729.json、图片生成/图生图/图像编辑(图加提示词即可实现图像编辑，无需mask)_1930500823778803713.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `ConditioningZeroOut`
- `DiptychCreate`
- `DualCLIPLoader`
- `FluxGuidance`
- `ICEFConditioning`
- `InContextEditInstruction`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCrop` —— 7/8 个有
- `MaskPreview` —— 7/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `ImageUpscaleWithModel` —— 4/8 个有
- `UpscaleModelLoader` —— 4/8 个有
- `ImageConcanate` —— 2/8 个有
- `ImageScaleDownToSize` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PMRF` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `TeaCache` —— 1/8 个有
- `easy imageInsetCrop` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 28 | 28 - 28 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 28，观测区间 28 - 28，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 28，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
