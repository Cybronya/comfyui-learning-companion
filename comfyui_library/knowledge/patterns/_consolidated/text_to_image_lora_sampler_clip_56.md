---
name: text_to_image_lora_sampler_clip_56
type: Text To Image
frequency: 14
level: strong
coverage: 0.892714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Seedance2.0文生视频｜高质量视频生成工作流_2095607601827504130.json, 视频生成/文生视频/Seedance2.5图生视频｜其它视频处理兼容｜首尾帧控制流畅自然_2102296652513103874.json, 视频生成/文生视频/Seedance2.5图生视频｜文生视频其它视频处理多面手_2097991912467816450.json, 视频生成/文生视频/Seedance2.5图生视频｜高清视频生成工作流制作_2096319929829126145.json, 视频生成/文生视频/Seedance2.5图生视频｜高质量AI视频生成新选择_2105123615518846977.json, 视频生成/文生视频/Seedance2.5多模态视频全构｜文生视频图生视频视频生视频｜三通道齐活_2102299674853076994.json, 视频生成/文生视频/Seedance2.5多模态视频工作流，文生视频图生视频视频生视频全覆盖_2103545826760024066.json, 视频生成/文生视频/Seedance2.5多模态视频工作流｜文生图生视频多模式生成_2097763010654851074.json, 视频生成/文生视频/Seedance2.5多模态视频｜文生图生视频生视频全覆盖_2105126628564226050.json, 视频生成/文生视频/Seedance2.5多模态视频｜文生视频视频生视频图生视频_2097931258201460738.json, 视频生成/文生视频/minimax_ref_fl低显存工作流｜真实感图生视频生成_2097834306843537409.json, 视频生成/文生视频/万相3.0参考生视频图生视频处理生成工作流_2101042889143971841.json, 视频生成/文生视频/多参视频生成｜Wan 3.0全节点注释三模合一_2092203862093549569.json, 视频生成/文生视频/多模态全能视频生成｜Seedance 2.5文生图生视频生视频工作流_2088341212158840834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/Seedance2.0文生视频｜高质量视频生成工作流_2095607601827504130.json、视频生成/文生视频/Seedance2.5图生视频｜其它视频处理兼容｜首尾帧控制流畅自然_2102296652513103874.json、视频生成/文生视频/Seedance2.5图生视频｜文生视频其它视频处理多面手_2097991912467816450.json、视频生成/文生视频/Seedance2.5图生视频｜高清视频生成工作流制作_2096319929829126145.json、视频生成/文生视频/Seedance2.5图生视频｜高质量AI视频生成新选择_2105123615518846977.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
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
- `LoadImage` —— 13/14 个有
- `LoadAudio` —— 9/14 个有
- `LoadVideo` —— 8/14 个有
- `RH_BytedanceSeedance25TokenMultimodalVideo` —— 7/14 个有
- `RH_BytedanceSeedance25TokenImageToVideo` —— 4/14 个有
- `SaveImage` —— 4/14 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `RH_RhartVideoSparkvideo20TextToVideo` —— 1/14 个有
- `Text` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
