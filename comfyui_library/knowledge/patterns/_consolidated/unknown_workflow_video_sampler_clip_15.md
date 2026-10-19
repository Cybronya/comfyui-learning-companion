---
name: unknown_workflow_video_sampler_clip_15
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.996474
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2010908567217381378.json, 视频生成/图生视频/1934184638036275202.json, 视频生成/图生视频/1933315042408312834.json, 视频生成/文生视频/1933102536746471425.json, 视频生成/文生视频/Self Forcing原生文生视频_2072999743049211904.json, 视频生成/文生视频/Wan2.1 文生视频【AI小王子】_1902942394851954690.json, 视频生成/文生视频/Wan2.1 文生视频工作流_1991075086629314562.json, 视频生成/文生视频/1904365052583907330.json, 视频生成/文生视频/Wan2.1-ComfyUI-Wan2.1(阿里万相)-最强开源文生视频_2053727976885366786.json, 视频生成/文生视频/Wan2.1文生视频_1985682376623828994.json, 视频生成/文生视频/Wan2.1文生视频_2008116883312087041.json, 视频生成/文生视频/文生视频 开源版_2046758506686058497.json, 视频生成/文生视频/文生视频+开源版 我的刀盾_2048961068537487362.json, 视频生成/文生视频/文生视频+开源版_2047284865078398977.json, 视频生成/文生视频/文生视频+开源版_2047564573158412289.json, 视频生成/文生视频/文生视频+开源版_2048571010336694273.json, 视频生成/文生视频/文生视频_1990234180640534529.json, 视频生成/文生视频/文生视频_2046503819072249858.json, 视频生成/文生视频/1958378106241368066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/2010908567217381378.json、视频生成/图生视频/1934184638036275202.json、视频生成/图生视频/1933315042408312834.json、视频生成/文生视频/1933102536746471425.json、视频生成/文生视频/Self Forcing原生文生视频_2072999743049211904.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 14/19 个有
- `VAEDecodeTiled` —— 14/19 个有
- `CM_IntToFloat` —— 13/19 个有
- `VAEDecode` —— 6/19 个有
- `ModelSamplingSD3` —— 4/19 个有
- `MagCache` —— 2/19 个有
- `WanVideoTeaCacheKJ` —— 2/19 个有
- `Fast Groups Bypasser (rgthree)` —— 1/19 个有
- `easy cleanGpuUsed` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 19 | 75% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 19 | 72% |
| 采样算法 | uni_pc | - | 19 | 79% |
| 调度器 | simple | - | 19 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 13/19 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 2/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，19 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，19 个样本
- 采样算法 最常用 uni_pc，19 个样本，一致性 79%
- 调度器 最常用 simple，19 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（13/19 个样本）：发现KSampler但没有VAEDecode
