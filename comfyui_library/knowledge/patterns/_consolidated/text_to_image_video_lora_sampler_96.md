---
name: text_to_image_video_lora_sampler_96
type: Text To Image
frequency: 8
level: strong
coverage: 0.916875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, ModelAttentionBackend, ModelPreviewOverrideKJ, UNETLoader, VAEDecode, VAELoader, easy modelLoaderPack, easy multiTrackEditor, easy multitrackProject, easy multitrackProjectVideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2107931825766232065.json, 视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506.json, 视频生成/图生视频/MiniMax-H3开源极简导演台｜战斗特效角色设计直出_2097966957537611777.json, 视频生成/图生视频/图像风格迁移转换工作流｜图片处理效果快速生成_2097813987210645506.json, 视频生成/文生视频/H3长视频自动化生成｜上下文分镜自由配置工作流_2095930333345701889.json, 视频生成/文生视频/MiniMax H3 Motion Context长视频生成工作流V2，文生视频图生视频方案_2103897957832683522.json, 视频生成/文生视频/RH-MINIMAX+H3+Motion+Context长视频V2｜连续剧情一键直出_2103664845823500290.json, 视频生成/文生视频/上下文分镜自由配置｜H3长视频自动化项目流三合一_2096213647822508034.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2107931825766232065.json、视频生成/图生视频/MiniMax H3长视频导演台EasyMedia Motion Context V2工作流，图生视_2108256036271509506.json、视频生成/图生视频/MiniMax-H3开源极简导演台｜战斗特效角色设计直出_2097966957537611777.json、视频生成/图生视频/图像风格迁移转换工作流｜图片处理效果快速生成_2097813987210645506.json、视频生成/文生视频/H3长视频自动化生成｜上下文分镜自由配置工作流_2095930333345701889.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy modelLoaderPack`
- `easy multiTrackEditor`
- `easy multitrackProject`
- `easy multitrackProjectVideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 6/8 个有
- `KSamplerSelect` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `SaveVideo` —— 6/8 个有
- `easy saveVideo` —— 6/8 个有
- `ManualSigmas` —— 4/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `easy blocker` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
