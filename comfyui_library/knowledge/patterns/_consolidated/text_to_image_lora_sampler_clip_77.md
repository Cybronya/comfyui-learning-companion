---
name: text_to_image_lora_sampler_clip_77
type: Text To Image
frequency: 15
level: weak
coverage: 0.865533
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Moss文生图 角色设计 三视图_2115816049546457090.json, 图片生成/图生图/Anima aesthetic-v11-全底模test-测试工作流_2079220135235252226.json, 图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json, 图片生成/文生图/Krea2 漫剧角色资产一键生成工作流｜文生四视图_2099740461484302337.json, 图片生成/文生图/MOSS image 最强开源文生图｜开源生图的黑马_2112029308096176130.json, 图片生成/文生图/MOSS image 最强开源文生图｜电商海报文字清晰_2112488209677635586.json, 图片生成/文生图/MOSS sft Comfyui官方流｜原汁原味官方文生图_2112425060618297345.json, 图片生成/文生图/MOSS 文生图新秀｜数字人全能助手一键出图_2112373662857908225.json, 图片生成/文生图/MOSS_4步_FP32模型VS25步_SFT模型文生图｜美少女写实两版对比_2114253844162113538.json, 图片生成/文生图/Moss Image文生图标准版 标准流程图像生成工具_2114124199613779970.json, 图片生成/文生图/Moss image SFT自动词优化文生图 提示词自动优化生成工具_2112985046939430913.json, 图片生成/文生图/Moss-image Base 基础文生图｜轻量快速出图首选_2112407813287931906.json, 图片生成/文生图/Moss-image Base 文生图入门款｜极简参数秒上手_2112420853316153345.json, 图片生成/文生图/flux3-image-klein文生图，高清创意形象直出_2111580915750236161.json, 数字人/数字人/MOSS好用的文生图，搭配数字人封面图一并搞定_2112700258626138114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/Moss文生图 角色设计 三视图_2115816049546457090.json、图片生成/图生图/Anima aesthetic-v11-全底模test-测试工作流_2079220135235252226.json、图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json、图片生成/文生图/Krea2 漫剧角色资产一键生成工作流｜文生四视图_2099740461484302337.json、图片生成/文生图/MOSS image 最强开源文生图｜开源生图的黑马_2112029308096176130.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 12/15 个有
- `JjkText` —— 10/15 个有
- `solarL_SaveImagesToZip` —— 10/15 个有
- `孤海注释` —— 10/15 个有
- `EmptyFlux2LatentImage` —— 9/15 个有
- `TextGenerate` —— 9/15 个有
- `PreviewAny` —— 8/15 个有
- `ResolutionSelector` —— 8/15 个有
- `SkipLayerGuidanceDiTSimple` —— 8/15 个有
- `PreviewImage` —— 7/15 个有
- `ComfySwitchNode` —— 3/15 个有
- `FastGroupsBypassSwitch` —— 2/15 个有
- `FluxResolutionNode` —— 2/15 个有
- `MuyeTextEditOutput` —— 2/15 个有
- `PrimitiveBoolean` —— 2/15 个有
- `XB_UNetNameBroadcaster` —— 2/15 个有
- `ImageBatch` —— 1/15 个有
- `StringFunction|pysssss` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 2000 | 15 | 0% |
| 高度 | 80 | 80 - 1600 | 15 | 0% |
| 采样步数 | 4 | 4 - 8 | 15 | 65% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 15 | 51% |
| 采样算法 | er_sde | - | 15 | 80% |
| 调度器 | beta | - | 15 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 2000，15 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1600，15 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，15 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，15 个样本
- 采样算法 最常用 er_sde，15 个样本，一致性 80%
- 调度器 最常用 beta，15 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（17/15 个样本）：Steps较低可能导致细节不足
