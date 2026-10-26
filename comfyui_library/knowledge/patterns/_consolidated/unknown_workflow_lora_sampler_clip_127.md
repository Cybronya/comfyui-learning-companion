---
name: unknown_workflow_lora_sampler_clip_127
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9756
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/文生视频工作流_2066457517043044354.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json, 视频生成/文生视频/最新Wan2.2文生视频_1949836969900687362.json, 视频生成/文生视频/电影分镜创作test_1982334497687519233.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/文生视频工作流_2066457517043044354.json、视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json、视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json、视频生成/文生视频/最新Wan2.2文生视频_1949836969900687362.json、视频生成/文生视频/电影分镜创作test_1982334497687519233.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/5 个有
- `SaveVideo` —— 3/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `Int` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 5 | 30% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 39% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，5 个样本，取值分散，一致性仅 30%
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
