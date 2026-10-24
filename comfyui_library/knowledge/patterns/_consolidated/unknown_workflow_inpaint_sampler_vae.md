---
name: unknown_workflow_inpaint_sampler_vae
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.9555
common_nodes: [DualCLIPLoader, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX局部重绘_1996155394600943617.json, 图片生成/图生图/Fill-removalV2-移除万物 _ 去水印 _ 抠图 _ 擦除_1993486322339872770.json, 图片生成/图生图/Nunchaku 万物消除强化加速版V5_1931170653636853762.json, 图片生成/图生图/Nunchaku 加速版万物消除V3(强化版)_1929441631513034754.json, 图片生成/图生图/Nunchaku+万物消除强化加速版V8_1931188076976996354.json, 图片生成/图生图/Nunchaku万物消除V2 加速版_1929715347270832129.json, 图片生成/图生图/【加速版】Nunchaku 修图 ｜消除图片中指定物体_1930802012533751809.json, 图片生成/图生图/图像水印去除_1940046980683010050.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_vae

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX局部重绘_1996155394600943617.json、图片生成/图生图/Fill-removalV2-移除万物 _ 去水印 _ 抠图 _ 擦除_1993486322339872770.json、图片生成/图生图/Nunchaku 万物消除强化加速版V5_1931170653636853762.json、图片生成/图生图/Nunchaku 加速版万物消除V3(强化版)_1929441631513034754.json、图片生成/图生图/Nunchaku+万物消除强化加速版V8_1931188076976996354.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 7/8 个有
- `FluxGuidance` —— 7/8 个有
- `NunchakuFluxLoraLoader` —— 7/8 个有
- `DifferentialDiffusion` —— 6/8 个有
- `CR Prompt Text` —— 4/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `CLIPTextEncodeFlux` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
