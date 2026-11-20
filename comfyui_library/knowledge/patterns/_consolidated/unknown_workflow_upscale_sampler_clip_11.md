---
name: unknown_workflow_upscale_sampler_clip_11
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.947364
common_nodes: [CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, GoohaiDisplayAny, RH_Screenwriter, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader, WujiCleaner, WujiImagePrompt2, WujiPromptEditor, WujiUpscaler2]
problems: []
missing: []
members: [图片生成/文生图/Moss-image sft+base融合文生微观世界六宫格_2116081058155417601.json, 图片生成/文生图/Moss-image sft+base融合文生微观世界六宫格_2116081672461578242.json, 图片生成/文生图/Moss-image sft+base融合文生角色五视图_2116069706602999810.json, 图片生成/文生图/Moss-image sft+base融合文生角色五视图_2116071187116806145.json, 图片生成/文生图/Moss-image sft+base融合文生角色定妆照_2114977925987655681.json, 图片生成/文生图/Moss-image sft+base融合文生角色定妆照_2116069187796951041.json, 图片生成/文生图/Moss-image_sft+base融合文生微观世界六宫格_2116354042967453697.json, 图片生成/文生图/Moss-image_sft+base融合文生微观世界六宫格_2116365826508017666.json, 图片生成/文生图/Moss-image_sft+base融合文生角色定妆照_2116355009439948801.json, 图片生成/文生图/Moss-image_sft+base融合文生角色定妆照_2116366755475054593.json, 图片生成/文生图/全能图片G2.0----官方稳定版_2116331904243949569.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Moss-image sft+base融合文生微观世界六宫格_2116081058155417601.json、图片生成/文生图/Moss-image sft+base融合文生微观世界六宫格_2116081672461578242.json、图片生成/文生图/Moss-image sft+base融合文生角色五视图_2116069706602999810.json、图片生成/文生图/Moss-image sft+base融合文生角色五视图_2116071187116806145.json、图片生成/文生图/Moss-image sft+base融合文生角色定妆照_2114977925987655681.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `GoohaiDisplayAny`
- `RH_Screenwriter`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `WujiImagePrompt2`
- `WujiPromptEditor`
- `WujiUpscaler2`

**可变部分**（部分 workflow 才有）：
- `WujiDesigner` —— 7/11 个有
- `PreviewImage` —— 3/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | beta57 | - | 11 | 100% |
| Prompt 约束强度(CFG) | 25 | 25 - 25 | 11 | 100% |
| 采样算法 | -1 | -1 - -1 | 11 | 100% |
| 调度器 | 1 | 1 - 1 | 11 | 100% |
| 重绘幅度 | 3 | 3 - 3 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 beta57，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，11 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 3，观测区间 3 - 3，11 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
