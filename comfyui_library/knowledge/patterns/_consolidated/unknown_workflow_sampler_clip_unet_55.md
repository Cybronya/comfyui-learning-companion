---
name: unknown_workflow_sampler_clip_unet_55
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.728267
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux3 Klein 文生图标准版_2113456940520132610.json, 图片生成/文生图/Flux3 Klein官方文生图_2112067434525061121.json, 图片生成/文生图/Flux3-Klein Text-to-Image 文生图工作流_2110954206533341186.json, 图片生成/文生图/Flux3-klein指定位置精准生成_2111266792965496834.json, 图片生成/文生图/Flux3-klein文生图PUP增强_2111479315035676674.json, 图片生成/文生图/MOSS SFT 提示增强标准文生图_2112193931260813313.json, 图片生成/文生图/MOSS SFT 文生图（Comfyui官方流）_2112379522267049985.json, 图片生成/文生图/MOSS SFT 文生图｜Comfyui官方流_2112066980613283842.json, 图片生成/文生图/MOSS sft Comfyui官方_2112031895180627969.json, 图片生成/文生图/MOSS sft Comfyui官方_2112119582155689986.json, 图片生成/文生图/MOSS sft Comfyui官方_2112423139555758082.json, 图片生成/文生图/MOSS sft Comfyui官方工作流文生图_2112510825444503554.json, 图片生成/文生图/MOSS-文生图-好_2112195416656793602.json, 图片生成/文生图/MOSS_BBOX 边界框精准布局 文生图工作流_2113954547713527809.json, 图片生成/文生图/文生图 角色设计 NB MOSS Sft_2112190645875068929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_55

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Flux3 Klein 文生图标准版_2113456940520132610.json、图片生成/文生图/Flux3 Klein官方文生图_2112067434525061121.json、图片生成/文生图/Flux3-Klein Text-to-Image 文生图工作流_2110954206533341186.json、图片生成/文生图/Flux3-klein指定位置精准生成_2111266792965496834.json、图片生成/文生图/Flux3-klein文生图PUP增强_2111479315035676674.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 13/15 个有
- `ResolutionSelector` —— 13/15 个有
- `SkipLayerGuidanceDiTSimple` —— 10/15 个有
- `ComfySwitchNode` —— 6/15 个有
- `PreviewImage` —— 5/15 个有
- `CreateBoundingBoxes` —— 3/15 个有
- `FastGroupsBypassSwitch` —— 2/15 个有
- `Flux3LayoutPrompt` —— 2/15 个有
- `Ideogram4PromptBuilderKJ` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `MOSSImageLayoutPrompt` —— 1/15 个有
- `孤海注释` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 15 - 50 | 15 | 60% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 15 | 63% |
| 采样算法 | er_sde | - | 15 | 73% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 15 - 50，15 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 73%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
