---
name: unknown_workflow_sampler_unet_vae_107
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.923182
common_nodes: [CLIPLoader, EmptyFlux2LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MOSS-Image｜50步原版 vs 8步DMD vs 4步Turbo·三档加速横评版_2113513165756657665.json, 视频生成/图生视频/MOSS-Image｜Base vs SFT 双模型同参对决·画质横评版_2113513180810014721.json, 视频生成/图生视频/MOSS-Image｜JSON Layout 结构化布局·图文排版控制版_2113513062564196353.json, 视频生成/图生视频/MOSS-Image｜SFT 50步高质量文生图·新手入门版_2113513200267382785.json, 视频生成/图生视频/MOSS-Image｜色彩深度LoRA·光影与色彩控制实验版_2113513044256059393.json, 视频生成/图生视频/MOSS_Beauty_人像美感创作_2114383210724552706.json, 视频生成/图生视频/MOSS_CharRef_角色参考生图_2114383277577560065.json, 视频生成/图生视频/MOSS_Kromoss_8Step_8步文生图_2114383185361588226.json, 视频生成/图生视频/MOSS_MAX_ULTRA_QHD_QHD高清生图_2114383254626324481.json, 视频生成/图生视频/MOSS_SFT_Style_Lab_SFT风格实验_2114383232941780993.json, 视频生成/图生视频/MOSS_StepLab_50_8_4_50·8·4步三档生图.json_2114383196866568194.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_107

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MOSS-Image｜50步原版 vs 8步DMD vs 4步Turbo·三档加速横评版_2113513165756657665.json、视频生成/图生视频/MOSS-Image｜Base vs SFT 双模型同参对决·画质横评版_2113513180810014721.json、视频生成/图生视频/MOSS-Image｜JSON Layout 结构化布局·图文排版控制版_2113513062564196353.json、视频生成/图生视频/MOSS-Image｜SFT 50步高质量文生图·新手入门版_2113513200267382785.json、视频生成/图生视频/MOSS-Image｜色彩深度LoRA·光影与色彩控制实验版_2113513044256059393.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `EmptyFlux2LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 10/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `SkipLayerGuidanceDiTSimple` —— 8/11 个有
- `FluxKontextImageScale` —— 1/11 个有
- `LoadImage` —— 1/11 个有
- `MOSSImageOstrisEditModelPatch` —— 1/11 个有
- `TextEncodeMOSSImageOstrisEdit` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 50 | 11 | 43% |
| Prompt 约束强度(CFG) | 3 | 1 - 3 | 11 | 64% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 50，11 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
