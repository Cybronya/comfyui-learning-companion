---
name: text_to_image_video_lora_sampler_18
type: Text To Image
frequency: 26
level: strong
coverage: 0.901192
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AIMixer导演台4step｜MiniMax H3图生视频创作_2090572888154927106.json, 视频生成/图生视频/H3导演台长视频生成段间引导turbo图生视频_2088250475895418882.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台全能参考加首尾帧全节点注释_2108635614169100290.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考加首尾帧_2111125388918349826.json, 视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考首尾帧全注释_2108428760713351170.json, 视频生成/图生视频/MiniMax H3导演台全能FL2V流程，图生视频导演级运镜大片感直出_2114470309234569217.json, 视频生成/图生视频/MiniMax H3导演台全能fl2v流程，图生视频导演级运镜_2110444159667625985.json, 视频生成/图生视频/MiniMax H3导演台全能工作流｜无水印版视频生成_2095281363539808258.json, 视频生成/图生视频/MiniMax H3视频生成导演台10.9优化乱说对白方案 数字人口播优化_2109031622308880385.json, 视频生成/图生视频/MiniMax_H3导演台全能fl2v流程，图生视频导演级运镜_2113816310248464385.json, 视频生成/图生视频/导演台AIMixer｜MiniMax H3 4step加速图生视频_2090886550669324290.json, 视频生成/图生视频/导演台长视频生成段间引导turbo｜H3数字人图生视频工作流_2088165576559652865.json, 视频生成/图生视频/段间引导turbo加速H3导演台长视频生成图生视频工作流_2088353948892749825.json, 视频生成/文生视频/H3视频生成导演台 文生视频图生视频多模态创作_2100649540188721154.json, 视频生成/文生视频/MiniMax H3 Director全能参考视频导演台 无水印输出版_2098271585596694529.json, 视频生成/文生视频/MiniMax H3 Max转场导演台全能参考首尾帧视频处理工具_2102145394816933889.json, 视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json, 视频生成/文生视频/MiniMax H3视频生成导演台｜文生视频视频生视频调度，镜头语言自己说了算_2100509465702387714.json, 视频生成/文生视频/fl2v全能导演台｜MiniMax H3文生视频生成_2091244438382268418.json, 视频生成/文生视频/fl2v全能工作流｜MiniMax H3导演台文生视频_2092705414675779585.json, 视频生成/文生视频/fl2v导演台全能｜MiniMax H3文生视频生成_2092894391294849025.json, 视频生成/文生视频/导演台全能工作流fl2v版｜MiniMax H3文生视频_2090908366989250561.json, 视频生成/文生视频/导演台全能工作流无水印版｜MiniMax H3三合一_2092367887234322434.json, 视频生成/文生视频/导演台无限长视频玩法｜MiniMax H3文生图生视频直出_2091281323360079874.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092724076027662337.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092927901426601985.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_18

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/AIMixer导演台4step｜MiniMax H3图生视频创作_2090572888154927106.json、视频生成/图生视频/H3导演台长视频生成段间引导turbo图生视频_2088250475895418882.json、视频生成/图生视频/MiniMax H3 max转场爆款导演台全能参考加首尾帧全节点注释_2108635614169100290.json、视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考加首尾帧_2111125388918349826.json、视频生成/图生视频/MiniMax H3 max转场爆款导演台｜全能参考首尾帧全注释_2108428760713351170.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 26 个 workflow 都包含：
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
- `孤海注释` —— 24/26 个有
- `MiniMaxH3DirectorRefine` —— 14/26 个有
- `UpscaleModelLoader` —— 14/26 个有
- `PathchSageAttentionKJ` —— 12/26 个有
- `SaveImage` —— 9/26 个有
- `LoadImage` —— 5/26 个有
- `CR Text` —— 4/26 个有
- `PreviewAny` —— 4/26 个有
- `Switch` —— 4/26 个有
- `DapaoImageSplitNode` —— 3/26 个有
- `PreviewImage` —— 2/26 个有
- `Label (rgthree)` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 26 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 26 | 100% |
| 采样算法 | er_sde | - | 26 | 100% |
| 调度器 | beta | - | 26 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| 宽度 | 80 | 80 - 80 | 26 | 100% |
| 高度 | 80 | 80 - 80 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，26 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，26 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，26 个样本，一致性 100%
- 调度器 最常用 beta，26 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，26 个样本，取值集中（一致性 100%）
- 高发问题（31/26 个样本）：Steps较低可能导致细节不足
