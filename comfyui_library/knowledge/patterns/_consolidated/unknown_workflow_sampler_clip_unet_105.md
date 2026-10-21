---
name: unknown_workflow_sampler_clip_unet_105
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.971429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/1949831170026594305.json, 视频生成/文生视频/1950182276686635009.json, 视频生成/文生视频/工作流视频篇1-阿里万相Wan2.2Al视频创作实战_2016870256769245185.json, 视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json, 视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2068556222554533890.json, 视频生成/文生视频/1949836969900687362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/1949831170026594305.json、视频生成/文生视频/1950182276686635009.json、视频生成/文生视频/工作流视频篇1-阿里万相Wan2.2Al视频创作实战_2016870256769245185.json、视频生成/文生视频/惊艳文生视频 Remix最新万相 Wan2.2-Remix-Comfy-T2V-文生视频_1998211525884174338.json、视频生成/文生视频/文生视频（解禁模型）：Wan2.2_Remix_2053378746035515394.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `CR Text` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageUpscaleWithModel` —— 1/7 个有
- `Int` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 57% |
| Prompt 约束强度(CFG) | 12 | 4 - 20 | 7 | 46% |
| 采样算法 | 3.5 | 1 - 3.5 | 7 | 49% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 12，观测区间 4 - 20，7 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 49%
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
