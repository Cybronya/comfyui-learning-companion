---
name: text_to_image_sampler_clip_unet_18
type: Text To Image
frequency: 18
level: weak
coverage: 0.897389
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json, 图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json, 图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json, 图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2107739693239590914.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2110564054040403969.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜_2111007985395916802.json, 图片生成/文生图/千问qwen-image-2.1文生图｜官方架构一键出图｜注意仅供学习不可商用_2104770730121588737.json, 图片生成/文生图/去AI感增强真实感工作流，MiniMax H3 LTX Wan图生视频动作迁移多合一_2103189879533424642.json, 图片生成/文生图/图图工作流人像写真｜Krea2文生图摄影出图_2095578272632496130.json, 图片生成/文生图/图图组合文生图玩法｜Krea2 多图融合一键出图_2096264881749184513.json, 图片生成/文生图/文生图ZImage工作流｜多段提示词同时出图神器_2100813214991863810.json, 图片生成/文生图/极速版Krea2 Trubo文生图｜美商极高V2版 美感直接拉满_2105551057450524673.json, 视频生成/文生视频/MiniMax H3 LTX Wan去AI感增强真实感视频处理工具_2102153536049082369.json, 视频生成/文生视频/MiniMax H3+LTX+Wan全家桶｜图生视频文生视频动作迁移三合一，去AI感增强真实感_2100439705560117249.json, 视频生成/文生视频/去AI感增强真实感合集｜MiniMax H3与LTX、Wan全模式生视频_2103071760437571586.json, 视频生成/文生视频/图生视频文生视频动作迁移去AI感增强真实感处理_2100637621520261121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json、图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json、图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json、图片生成/文生图/千问qwen-image-2.1文生图工作流_2104553799485583362.json、图片生成/文生图/千问qwen-image-2.1文生图工作流（不可商用）_2101941085793771521.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 17/18 个有
- `SaveImage` —— 15/18 个有
- `JjkText` —— 13/18 个有
- `solarL_SaveImagesToZip` —— 13/18 个有
- `ConditioningZeroOut` —— 10/18 个有
- `孤海注释` —— 10/18 个有
- `PreviewImage` —— 8/18 个有
- `RHHiddenNodes` —— 5/18 个有
- `VHS_LoadVideo` —— 5/18 个有
- `VHS_VideoCombine` —— 5/18 个有
- `ModelSamplingAuraFlow` —— 2/18 个有
- `TextEncodeQwenImageEditPlus` —— 2/18 个有
- `DyPE_FLUX` —— 1/18 个有
- `PromptBatchQueue` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 18 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 18 | 61% |
| 采样算法 | er_sde | - | 18 | 72% |
| 调度器 | beta | - | 18 | 72% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 1440 | 18 | 0% |
| 高度 | 80 | 80 - 1920 | 18 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，18 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，18 个样本
- 采样算法 最常用 er_sde，18 个样本，一致性 72%
- 调度器 最常用 beta，18 个样本，一致性 72%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1440，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，18 个样本，取值分散，一致性仅 0%
- 高发问题（21/18 个样本）：Steps较低可能导致细节不足
