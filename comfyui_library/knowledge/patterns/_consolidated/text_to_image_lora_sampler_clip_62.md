---
name: text_to_image_lora_sampler_clip_62
type: Text To Image
frequency: 16
level: strong
coverage: 0.877188
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/官方稳定版全能视频X图生视频创意生成工作流_2088405018243325953.json, 图片生成/图生图/官方稳定版图生视频｜全能视频X其它图片处理其他创意工作流_2088383430127079426.json, 图片生成/图生图/宠物拟人工作流｜毛孩子照片秒变拟人角色，新奇创意_2099899324359602178.json, 图片生成/图生图/室内效果图分阶修复专家｜精修图生图 老房子秒变样板间_2105510590549676033.json, 图片生成/图生图/建筑效果图重新渲染｜光源布光自由控制重出图_2101547236311257089.json, 图片生成/图生图/手办创建_2108026254615203841.json, 图片生成/图生图/手办创建图生图，照片一键变收藏级手办模型_2112272916351111169.json, 图片生成/图生图/手办创建工作流｜图生图一键生成手办设计稿_2114066290829783041.json, 图片生成/图生图/换下装裤子裙子替换生成｜Image2下装设计_2094556599502327810.json, 图片生成/图生图/照片光影重构十种风格图生图处理生成工作流工具_2101763548941733889.json, 图片生成/图生图/照片渲染灯光自由控｜图生图按心意调整光源氛围_2101542677861986306.json, 图片生成/图生图/空白工作流_2112112425230225410.json, 图片生成/图生图/角色战技连招设定卡Seedance与MiniMax H3图生图工具_2101008188308017153.json, 图片生成/图生图/角色战技连招设定卡生成｜Seedance2.0与MiniMaxH3专用_2096718130381938689.json, 图片生成/图生图/角色战技连招设定卡｜Seedance2.0与2.5及MiniMaxH3专用_2100765592633569281.json, 图片生成/文生图/全能图片G2.5多宫格故事板 Seedance2.0_2.5与H3通用分镜_2098702107397414913.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/官方稳定版全能视频X图生视频创意生成工作流_2088405018243325953.json、图片生成/图生图/官方稳定版图生视频｜全能视频X其它图片处理其他创意工作流_2088383430127079426.json、图片生成/图生图/宠物拟人工作流｜毛孩子照片秒变拟人角色，新奇创意_2099899324359602178.json、图片生成/图生图/室内效果图分阶修复专家｜精修图生图 老房子秒变样板间_2105510590549676033.json、图片生成/图生图/建筑效果图重新渲染｜光源布光自由控制重出图_2101547236311257089.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 15/16 个有
- `SaveImage` —— 14/16 个有
- `RH_RhartImageG2ImageToImage` —— 7/16 个有
- `PrimitiveStringMultiline` —— 5/16 个有
- `RH_RhartImageG25SunburstImageToImage` —— 4/16 个有
- `WujiUpscaler` —— 3/16 个有
- `CheckpointLoaderSimple` —— 2/16 个有
- `RHHiddenNodes` —— 2/16 个有
- `RH_RhartVideoGOfficialImageToVideo` —— 2/16 个有
- `SaveVideo` —— 2/16 个有
- `TextEncodeQwenImageEditPlus` —— 2/16 个有
- `RH_SeedreamV5ProImageToImage` —— 1/16 个有
- `ShowText|pysssss` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 16 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 16 | 100% |
| 采样算法 | er_sde | - | 16 | 100% |
| 调度器 | beta | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 80 | 80 - 80 | 16 | 100% |
| 高度 | 80 | 80 - 80 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，16 个样本，一致性 100%
- 调度器 最常用 beta，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，16 个样本，取值集中（一致性 100%）
- 高发问题（19/16 个样本）：Steps较低可能导致细节不足
