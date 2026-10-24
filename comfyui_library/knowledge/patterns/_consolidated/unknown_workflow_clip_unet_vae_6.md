---
name: unknown_workflow_clip_unet_vae_6
type: Unknown Workflow
frequency: 10
level: weak
coverage: 0.9853
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2文生视频工作流_2011408541554315266.json, 图片生成/文生图/wan2.1_t2v1_3B提升本地运行速度_1902941440509382658.json, 图片生成/文生图/wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json, 图片生成/文生图/wan22文生图_1950527410125066242.json, 图片生成/文生图/万相2.2 高质量文生图工作流_1950184764194119681.json, 视频生成/文生视频/AAiwood wan2.2+2.1二阶文生视频_1949875905322729473.json, 视频生成/文生视频/ComfyUI官方文生视频工作流_2050448250037121026.json, 视频生成/文生视频/Self Forcing原生文生视频_1933102536746471425.json, 视频生成/文生视频/WAN14B-文生视频_1949853875865042945.json, 视频生成/文生视频/万相 Wan2.2 14B文生视频工作流_1949831170026594305.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Wan2.2文生视频工作流_2011408541554315266.json、图片生成/文生图/wan2.1_t2v1_3B提升本地运行速度_1902941440509382658.json、图片生成/文生图/wan2.1_官方工作流_T2V_文字到视频_1930295791557185537.json、图片生成/文生图/wan22文生图_1950527410125066242.json、图片生成/文生图/万相2.2 高质量文生图工作流_1950184764194119681.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 8/10 个有
- `KSampler` —— 5/10 个有
- `KSamplerAdvanced` —— 5/10 个有
- `SaveImage` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `LoadImage` —— 1/10 个有
- `SaveAnimatedWEBP` —— 1/10 个有
- `TeaCache` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 5 | 41% |
| Prompt 约束强度(CFG) | 6 | 1 - 20 | 10 | 23% |
| 采样算法 | 3.5 | 1 - 3.5 | 5 | 67% |
| 调度器 | simple | - | 10 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，5 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 20，10 个样本，取值分散，一致性仅 23%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，5 个样本
- 调度器 最常用 simple，10 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
