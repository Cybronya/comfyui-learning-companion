---
name: unknown_workflow_lora_sampler_unet_263
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.769
common_nodes: [Any Switch (rgthree), CLIPLoader, DapaoImagePadDirectionNode, Image Comparer (rgthree), ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, Switch any [Crystools], TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, 孤海注释, 忽略多组孤海, 长边短边]
problems: []
missing: []
members: [图片生成/图生图/Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961.json, 图片生成/图生图/千问Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2113826658422710274.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_263

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2111962967242792961.json、图片生成/图生图/千问Qwen image 2.1 高质量无痕扩图｜指定扩图大小｜指定图像比例｜零偏移｜零色差_2113826658422710274.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `DapaoImagePadDirectionNode`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Switch any [Crystools]`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`
- `忽略多组孤海`
- `长边短边`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
