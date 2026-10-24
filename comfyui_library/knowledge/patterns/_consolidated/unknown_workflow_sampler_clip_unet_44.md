---
name: unknown_workflow_sampler_clip_unet_44
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.749471
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Flux 3_Image_Klein开源版-文生图_2111064999098671105.json, 图片生成/文生图/Flux-Kelin--文生图_2034949979520901121.json, 图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json, 图片生成/文生图/Flux3 Klein官方文生图_2112067434525061121.json, 图片生成/文生图/Flux3-Klein Text-to-Image 文生图工作流_2110954206533341186.json, 图片生成/文生图/Flux3-klein指定位置精准生成_2111266792965496834.json, 图片生成/文生图/Flux3-klein文生图PUP增强_2111479315035676674.json, 图片生成/文生图/MOSS SFT 文生图（Comfyui官方流）_2112379522267049985.json, 图片生成/文生图/MOSS SFT 文生图｜Comfyui官方流_2112066980613283842.json, 图片生成/文生图/MOSS sft Comfyui官方_2112031895180627969.json, 图片生成/文生图/MOSS sft Comfyui官方_2112119582155689986.json, 图片生成/文生图/MOSS sft Comfyui官方_2112423139555758082.json, 图片生成/文生图/MOSS sft Comfyui官方工作流文生图_2112510825444503554.json, 图片生成/文生图/MOSS-文生图-好_2112195416656793602.json, 图片生成/文生图/flux3 t2v 蒸馏版本_2111318527201341441.json, 图片生成/文生图/flux3_klein 文生图 base版本_2110956211372904449.json, 图片生成/文生图/文生图 角色设计 NB MOSS Sft_2112190645875068929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_44

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Flux 3_Image_Klein开源版-文生图_2111064999098671105.json、图片生成/文生图/Flux-Kelin--文生图_2034949979520901121.json、图片生成/文生图/Flux3 Image Klein distill t2i加速文生图_2110971162019848193.json、图片生成/文生图/Flux3 Klein官方文生图_2112067434525061121.json、图片生成/文生图/Flux3-Klein Text-to-Image 文生图工作流_2110954206533341186.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 16/17 个有
- `TextGenerate` —— 15/17 个有
- `PreviewAny` —— 13/17 个有
- `ResolutionSelector` —— 13/17 个有
- `SkipLayerGuidanceDiTSimple` —— 8/17 个有
- `ComfySwitchNode` —— 6/17 个有
- `PreviewImage` —— 6/17 个有
- `Ideogram4PromptBuilderKJ` —— 3/17 个有
- `CreateBoundingBoxes` —— 2/17 个有
- `FastGroupsBypassSwitch` —— 2/17 个有
- `Flux3LayoutPrompt` —— 1/17 个有
- `JjkText` —— 1/17 个有
- `孤海注释` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 8 - 50 | 17 | 51% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 17 | 53% |
| 采样算法 | er_sde | - | 17 | 65% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 50，观测区间 8 - 50，17 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，17 个样本
- 采样算法 最常用 er_sde，17 个样本，一致性 65%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
