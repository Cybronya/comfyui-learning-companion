---
name: unknown_workflow_sampler_clip_unet_11
type: Unknown Workflow
frequency: 31
level: moderate
coverage: 0.774871
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KOOK-MOSS-Base-观澜_2115657543379935234.json, 图片生成/文生图/KOOK-MOSS-SFT-观澜_2112403091164319745.json, 图片生成/文生图/MOSS IMAGE 文生图_2113649019552624641.json, 图片生成/文生图/MOSS SFT 提示增强标准文生图_2112193931260813313.json, 图片生成/文生图/MOSS SFT 文生图（Comfyui官方流）_2112379522267049985.json, 图片生成/文生图/MOSS SFT 文生图｜Comfyui官方流_2112066980613283842.json, 图片生成/文生图/MOSS Text-to-Image 2K Turbo Edition 图生图2K极速版_2113063260466536449.json, 图片生成/文生图/MOSS image文生图极速版（带提示词优化）_2113112082550976514.json, 图片生成/文生图/MOSS sft Comfyui官方_2112031895180627969.json, 图片生成/文生图/MOSS sft Comfyui官方_2112119582155689986.json, 图片生成/文生图/MOSS sft Comfyui官方_2112423139555758082.json, 图片生成/文生图/MOSS sft Comfyui官方工作流文生图_2112510825444503554.json, 图片生成/文生图/MOSS-Base-文生图_2115751393586929666.json, 图片生成/文生图/MOSS-Base-文生图_2115803286438760450.json, 图片生成/文生图/MOSS-Image 文生图_2114895113712394241.json, 图片生成/文生图/MOSS-文生图-好_2112195416656793602.json, 图片生成/文生图/MOSS_sft_Comfyui官方工作流文生图_2115239110100213762.json, 图片生成/文生图/Moss Image 文生图标准版_2113450821328392193.json, 图片生成/文生图/Moss-image-base文生图3D国漫CG风格_2116146128541544450.json, 图片生成/文生图/Moss-image-base文生图赛璐璐平涂动漫风格_2116096666603446273.json, 图片生成/文生图/Moss-image-base文生图超写实真人摄影风格_2116212220819496961.json, 图片生成/文生图/Moss_Image_sft_turbo8步加速工作流_2113398897551958018.json, 图片生成/文生图/Moss_Image_sft_turbo加速工作流_2113109058533285889.json, 图片生成/文生图/Moss_Image_sft图像生产工作流_2112494670994567169.json, 图片生成/文生图/moss_image图像生成_2112202038108049409.json, 图片生成/文生图/moss文生图_2113583535255805954.json, 图片生成/文生图/文生图 角色设计 NB MOSS Sft_2112190645875068929.json, 图片生成/文生图/（自用-贞贞版）Moss-image Sft Fixed文生图_2112438870972387329.json, 平台全量/ERNIE_Image_T2I_2119042179208404993.json, 平台全量/MOSS 文生图与提示词增强_2119876525502844930.json, 平台全量/MOSS 日系摄影风格_2119876651923361794.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_11

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（图片生成/文生图/KOOK-MOSS-Base-观澜_2115657543379935234.json、图片生成/文生图/KOOK-MOSS-SFT-观澜_2112403091164319745.json、图片生成/文生图/MOSS IMAGE 文生图_2113649019552624641.json、图片生成/文生图/MOSS SFT 提示增强标准文生图_2112193931260813313.json、图片生成/文生图/MOSS SFT 文生图（Comfyui官方流）_2112379522267049985.json…）

- **类型**：Unknown Workflow
- **样本数**：31
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 31 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 29/31 个有
- `PrimitiveStringMultiline` —— 26/31 个有
- `SkipLayerGuidanceDiTSimple` —— 26/31 个有
- `TextGenerate` —— 24/31 个有
- `PreviewAny` —— 22/31 个有
- `ComfySwitchNode` —— 17/31 个有
- `LoraLoaderModelOnly` —— 14/31 个有
- `PrimitiveBoolean` —— 8/31 个有
- `PreviewImage` —— 6/31 个有
- `FastGroupsBypassSwitch` —— 2/31 个有
- `LoadImage` —— 2/31 个有
- `孤海注释` —— 2/31 个有
- `QwenImagePromptOptimizer` —— 1/31 个有
- `StringReplace` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 50 | 31 | 44% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 31 | 67% |
| 采样算法 | er_sde | - | 31 | 87% |
| 调度器 | simple | - | 31 | 97% |
| 重绘幅度 | 1 | 1 - 1 | 31 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 50，31 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，31 个样本
- 采样算法 最常用 er_sde，31 个样本，一致性 87%
- 调度器 最常用 simple，31 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
