---
name: unknown_workflow_inpaint_sampler_clip_21
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.909875
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, FluxGuidance, InpaintModelConditioning, KSampler, MaskBlur+, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/z-image输入base64工作流_2008785069535666178.json, 图片生成/图生图/z-image输入base64工作流_2008825724299386882.json, 图片生成/图生图/zimage重绘_2044459125228179458.json, 图片生成/图生图/局部重绘_2001620631345065986.json, 图片生成/图生图/局部重绘_Z-image_Base_万能迁移_局部重绘_极速版_真实自然无痕_2116134172938031106.json, 图片生成/图生图/极简Z-image局部重绘_1999059377522868226.json, 图片生成/图生图/画面修改 局部重绘  Z-image_2019615234633240578.json, 图片生成/文生图/Z_mage局部重绘_1995377541710012417.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/z-image输入base64工作流_2008785069535666178.json、图片生成/图生图/z-image输入base64工作流_2008825724299386882.json、图片生成/图生图/zimage重绘_2044459125228179458.json、图片生成/图生图/局部重绘_2001620631345065986.json、图片生成/图生图/局部重绘_Z-image_Base_万能迁移_局部重绘_极速版_真实自然无痕_2116134172938031106.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `MaskBlur+`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/8 个有
- `ETN_LoadImageBase64` —— 2/8 个有
- `ETN_LoadMaskBase64` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `GetNode` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ImageStitch` —— 1/8 个有
- `MaskPreview` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `TextInput_` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 8 | 97% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 0.85 | 0.85 - 0.87 | 8 | 99% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，8 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 0.85，观测区间 0.85 - 0.87，8 个样本，取值集中（一致性 99%）
