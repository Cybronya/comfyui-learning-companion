---
name: unknown_workflow_sampler_clip_unet_291
type: Unknown Workflow
frequency: 4
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, Flux2KleinEnhancer, Flux2KleinKSamplerExperimental, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键质感修复｜人像洗图增强Flux2-Klein_2097885143288602626.json, 图片生成/图生图/一键质感修复｜人像洗图增强Flux2-Klein_2099413868543037442.json, 图片生成/图生图/老照片修复｜一键翻新上色去划痕Flux2-Klein_2096502531819139073.json, 图片生成/图生图/老照片修复｜一键翻新上色去划痕Flux2-Klein_2096808460695461889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_291

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键质感修复｜人像洗图增强Flux2-Klein_2097885143288602626.json、图片生成/图生图/一键质感修复｜人像洗图增强Flux2-Klein_2099413868543037442.json、图片生成/图生图/老照片修复｜一键翻新上色去划痕Flux2-Klein_2096502531819139073.json、图片生成/图生图/老照片修复｜一键翻新上色去划痕Flux2-Klein_2096808460695461889.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2KleinEnhancer`
- `Flux2KleinKSamplerExperimental`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 0.65 | 0.6 - 0.7 | 4 | 92% |
| 采样算法 | 0.5 | 0.5 - 0.5 | 4 | 100% |
| 调度器 | 1.15 | 1.15 - 1.15 | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 0.65，观测区间 0.6 - 0.7，4 个样本，取值集中（一致性 92%）
- 采样算法 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1.15，观测区间 1.15 - 1.15，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.6，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
