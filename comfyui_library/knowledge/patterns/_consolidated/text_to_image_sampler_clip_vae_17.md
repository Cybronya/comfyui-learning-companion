---
name: text_to_image_sampler_clip_vae_17
type: Text To Image
frequency: 7
level: weak
coverage: 0.910857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/分镜图生成_2093149514755559425.json, 视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json, 视频生成/文生视频/完美中文理解领军模型｜Qwen2512文生图千问旗舰_2090825263516045313.json, 视频生成/文生视频/导演台无限长视频玩法｜MiniMax H3文生图生视频直出_2091281323360079874.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092724076027662337.json, 视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092927901426601985.json, 视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/分镜图生成_2093149514755559425.json、视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json、视频生成/文生视频/完美中文理解领军模型｜Qwen2512文生图千问旗舰_2090825263516045313.json、视频生成/文生视频/导演台无限长视频玩法｜MiniMax H3文生图生视频直出_2091281323360079874.json、视频生成/文生视频/无限长视频玩法｜MiniMax H3导演台文生视频_2092724076027662337.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `UNETLoader` —— 6/7 个有
- `JjkText` —— 5/7 个有
- `solarL_SaveImagesToZip` —— 5/7 个有
- `孤海注释` —— 5/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `MiniMaxH3Director` —— 3/7 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `EmptyHunyuanLatentVideo` —— 1/7 个有
- `EnhancedLoadDiffusionModel` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `WanVideoTeaCacheKJ` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 7 | 0% |
| 高度 | 80 | 80 - 1536 | 7 | 0% |
| 采样步数 | 4 | 4 - 35 | 7 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3.5 - 4.5 | 7 | 92% |
| 采样算法 | er_sde | - | 7 | 71% |
| 调度器 | beta | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，7 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 35，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3.5 - 4.5，7 个样本，取值集中（一致性 92%）
- 采样算法 最常用 er_sde，7 个样本，一致性 71%
- 调度器 最常用 beta，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
