---
name: unknown_workflow_video_clip_unet_4
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.986533
common_nodes: [CLIPLoader, CLIPTextEncode, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1902941440509382658.json, 图片生成/文生图/1930295791557185537.json, 图片生成/文生图/1951273402428502018.json, 图片生成/文生图/Wan2.2文生视频工作流_2011408541554315266.json, 视频生成/图生视频/1951274276659867650.json, 视频生成/图生视频/1951804301834440706.json, 视频生成/图生视频/1987307533339701250.json, 视频生成/图生视频/1951277844100009986.json, 视频生成/图生视频/1952539360614920193.json, 视频生成/图生视频/1991844034222288897.json, 视频生成/图生视频/2043858986851639297.json, 视频生成/图生视频/2043862678724157442.json, 视频生成/文生视频/1950378020252073986.json, 视频生成/文生视频/1949853875865042945.json, 视频生成/文生视频/Wan2.2官网14B图生视频&文生视频&5B文or图生视频_2072999658865336320.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/1902941440509382658.json、图片生成/文生图/1930295791557185537.json、图片生成/文生图/1951273402428502018.json、图片生成/文生图/Wan2.2文生视频工作流_2011408541554315266.json、视频生成/图生视频/1951274276659867650.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 14/15 个有
- `LoadImage` —— 11/15 个有
- `EmptyHunyuanLatentVideo` —— 8/15 个有
- `Wan22ImageToVideoLatent` —— 7/15 个有
- `WanImageToVideo` —— 6/15 个有
- `KSamplerAdvanced` —— 3/15 个有
- `SaveImage` —— 2/15 个有
- `CR Text` —— 1/15 个有
- `LoraLoaderModelOnly` —— 1/15 个有
- `SaveAnimatedWEBP` —— 1/15 个有
- `TeaCache` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 30 | 14 | 38% |
| Prompt 约束强度(CFG) | 5 | 1 - 20 | 15 | 6% |
| 采样算法 | uni_pc | - | 15 | 60% |
| 调度器 | simple | - | 15 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 30，14 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 20，15 个样本，取值分散，一致性仅 6%
- 采样算法 最常用 uni_pc，15 个样本，一致性 60%
- 调度器 最常用 simple，15 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
