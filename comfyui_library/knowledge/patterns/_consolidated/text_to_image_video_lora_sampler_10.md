---
name: text_to_image_video_lora_sampler_10
type: Text To Image
frequency: 29
level: strong
coverage: 0.897724
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AIMixer导演台4step｜MiniMax H3图生视频创作_2090572888154927106.json, 视频生成/图生视频/H3导演台长视频生成段间引导turbo图生视频_2088250475895418882.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台全能参考加首尾帧全节点注释_2108635614169100290.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考加首尾帧_2111125388918349826.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考首尾帧全注释_2108428760713351170.json, 视频生成/图生视频/MiniMax H3导演台全能fl2v流程，图生视频导演级运镜_2110444159667625985.json, 视频生成/图生视频/MiniMax H3导演台全能工作流｜无水印版视频生成_2095281363539808258.json, 视频生成/图生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json, 视频生成/图生视频/MiniMax H3视频生成导演台10.9优化乱说对白方案 数字人口播优化_2109031622308880385.json, 视频生成/图生视频/导演台AIMixer｜MiniMax H3 4step加速图生视频_2090886550669324290.json, 视频生成/图生视频/导演台长视频生成段间引导turbo｜H3数字人图生视频工作流_2088165576559652865.json, 视频生成/图生视频/无水印导演台全能流｜MiniMax H3开源角色设计图生视频_2092719967396524033.json, 视频生成/图生视频/无水印版开源导演台｜MiniMax H3场景特效图生视频_2092919674605498369.json, 视频生成/图生视频/段间引导turbo加速H3导演台长视频生成图生视频工作流_2088353948892749825.json, 视频生成/文生视频/H3图生视频高清版 无水印高清视频生成工具_2099215533198635010.json, 视频生成/文生视频/H3图生视频高清版 无水印高清视频生成工具_2099595930357035010.json, 视频生成/文生视频/H3视频生成导演台 文生视频图生视频多模态创作_2100649540188721154.json, 视频生成/文生视频/MiniMax H3 Director全能参考视频导演台 无水印输出版_2098271585596694529.json, 视频生成/文生视频/MiniMax H3 Max转场导演台全能参考首尾帧视频处理工具_2102145394816933889.json, 视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json, 视频生成/文生视频/MiniMax H3视频生成导演台｜文生视频视频生视频调度，镜头语言自己说了算_2100509465702387714.json, 视频生成/文生视频/fl2v全能导演台｜MiniMax H3文生视频生成_2091244438382268418.json, 视频生成/文生视频/fl2v全能工作流｜MiniMax H3导演台文生视频_2092705414675779585.json, 视频生成/文生视频/fl2v导演台全能｜MiniMax H3文生视频生成_2092894391294849025.json, 视频生成/文生视频/导演台全能工作流fl2v版｜MiniMax H3文生视频_2090908366989250561.json, 视频生成/文生视频/导演台全能工作流无水印版｜MiniMax H3三合一_2092367887234322434.json, 视频生成/文生视频/导演台无限长视频玩法｜MiniMax H3文生图生视频直出_2091281323360079874.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092724076027662337.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092927901426601985.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（视频生成/图生视频/AIMixer导演台4step｜MiniMax H3图生视频创作_2090572888154927106.json、视频生成/图生视频/H3导演台长视频生成段间引导turbo图生视频_2088250475895418882.json、视频生成/图生视频/MiniMax H3 max转场爆款导演台全能参考加首尾帧全节点注释_2108635614169100290.json、视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考加首尾帧_2111125388918349826.json、视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考首尾帧全注释_2108428760713351170.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 29 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 27/29 个有
- `MiniMaxH3DirectorRefine` —— 16/29 个有
- `UpscaleModelLoader` —— 16/29 个有
- `PathchSageAttentionKJ` —— 13/29 个有
- `SaveImage` —— 10/29 个有
- `CR Text` —— 4/29 个有
- `LoadImage` —— 4/29 个有
- `PreviewAny` —— 4/29 个有
- `Switch` —— 4/29 个有
- `DapaoImageSplitNode` —— 1/29 个有
- `Label (rgthree)` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高发问题（33/29 个样本）：Steps较低可能导致细节不足
