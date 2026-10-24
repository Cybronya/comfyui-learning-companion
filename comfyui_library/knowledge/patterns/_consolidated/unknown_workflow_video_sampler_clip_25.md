---
name: unknown_workflow_video_sampler_clip_25
type: Unknown Workflow
frequency: 17
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/Wan2.1+文生视频  高清流畅版_2010908567217381378.json, 视频生成/图生视频/【老金驿站】高清WANt2v高速Magcache生成工作流_1934184638036275202.json, 视频生成/图生视频/最新MagCache视频加速-文生视频_1933315042408312834.json, 视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json, 视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json, 视频生成/文生视频/Wan2.1(阿里万相)-文生视频_Comfyui工作流_1904365052583907330.json, 视频生成/文生视频/Wan2.1+文生视频高清动态视频_2010596616985649154.json, 视频生成/文生视频/Wan2.1文生视频_1985682376623828994.json, 视频生成/文生视频/Wan2.1文生视频_2008116883312087041.json, 视频生成/文生视频/文生视频 开源版_2046758506686058497.json, 视频生成/文生视频/文生视频+开源版 我的刀盾_2048961068537487362.json, 视频生成/文生视频/文生视频+开源版_2047284865078398977.json, 视频生成/文生视频/文生视频+开源版_2047564573158412289.json, 视频生成/文生视频/文生视频+开源版_2048571010336694273.json, 视频生成/文生视频/文生视频_1990234180640534529.json, 视频生成/文生视频/文生视频_2046503819072249858.json, 视频生成/文生视频/文生视频_Comfyui工作流_1958378106241368066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_25

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/Wan2.1+文生视频  高清流畅版_2010908567217381378.json、视频生成/图生视频/【老金驿站】高清WANt2v高速Magcache生成工作流_1934184638036275202.json、视频生成/图生视频/最新MagCache视频加速-文生视频_1933315042408312834.json、视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json、视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 13/17 个有
- `VAEDecodeTiled` —— 13/17 个有
- `CM_IntToFloat` —— 12/17 个有
- `VAEDecode` —— 5/17 个有
- `WanVideoTeaCacheKJ` —— 3/17 个有
- `MagCache` —— 2/17 个有
- `ModelSamplingSD3` —— 2/17 个有
- `easy cleanGpuUsed` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 25 - 30 | 17 | 96% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 17 | 100% |
| 采样算法 | uni_pc | - | 17 | 82% |
| 调度器 | simple | - | 17 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 12/17 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 30，观测区间 25 - 30，17 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，17 个样本，一致性 82%
- 调度器 最常用 simple，17 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（12/17 个样本）：发现KSampler但没有VAEDecode
