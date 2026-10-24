---
name: text_to_image_lora_sampler_clip_88
type: Text To Image
frequency: 15
level: strong
coverage: 0.871867
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Seedance2.0文生视频｜高质量视频生成工作流_2095607601827504130.json, 视频生成/文生视频/Seedance2.5图生视频工作流，高质量图像到视频生成方案_2103542632843669506.json, 视频生成/文生视频/Seedance2.5图生视频工作流｜高质量图像驱动视频生成_2097761537908887554.json, 视频生成/文生视频/Seedance2.5图生视频｜其它视频处理兼容｜首尾帧控制流畅自然_2102296652513103874.json, 视频生成/文生视频/Seedance2.5图生视频｜文生视频其它视频处理多面手_2097991912467816450.json, 视频生成/文生视频/Seedance2.5图生视频｜高清视频生成工作流制作_2096319929829126145.json, 视频生成/文生视频/Seedance2.5图生视频｜高质量AI视频生成新选择_2105123615518846977.json, 视频生成/文生视频/Seedance2.5多模态视频工作流，文生视频图生视频视频生视频全覆盖_2103545826760024066.json, 视频生成/文生视频/Seedance2.5多模态视频工作流｜文生图生视频多模式生成_2097763010654851074.json, 视频生成/文生视频/Seedance2.5多模态视频｜文生图生视频生视频全覆盖_2105126628564226050.json, 视频生成/文生视频/Seedance2.5多模态视频｜文生视频视频生视频图生视频_2097931258201460738.json, 视频生成/文生视频/minimax_ref_fl低显存工作流｜真实感图生视频生成_2097834306843537409.json, 视频生成/文生视频/万相3.0参考生视频图生视频处理生成工作流_2101042889143971841.json, 视频生成/文生视频/全能参考生视频2K版｜海螺MiniMaxH3官方多图音视频参考_2088745519744110594.json, 视频生成/文生视频/视频生成2KMiniMaxH3版ENG海螺_2087117391724634114.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_88

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/Seedance2.0文生视频｜高质量视频生成工作流_2095607601827504130.json、视频生成/文生视频/Seedance2.5图生视频工作流，高质量图像到视频生成方案_2103542632843669506.json、视频生成/文生视频/Seedance2.5图生视频工作流｜高质量图像驱动视频生成_2097761537908887554.json、视频生成/文生视频/Seedance2.5图生视频｜其它视频处理兼容｜首尾帧控制流畅自然_2102296652513103874.json、视频生成/文生视频/Seedance2.5图生视频｜文生视频其它视频处理多面手_2097991912467816450.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `LoadAudio` —— 8/15 个有
- `LoadVideo` —— 8/15 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 6/15 个有
- `SaveImage` —— 6/15 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 5/15 个有
- `PlaySound|pysssss` —— 2/15 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 2/15 个有
- `MuyeTextEditOutput` —— 1/15 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 1/15 个有
- `RH_RhartVideoSparkvideo20TextToVideo` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
