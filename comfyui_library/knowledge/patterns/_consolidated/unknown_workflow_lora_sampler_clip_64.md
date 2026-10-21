---
name: unknown_workflow_lora_sampler_clip_64
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.954167
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1963965754733416450.json, 视频生成/图生视频/1956634658516471809.json, 视频生成/图生视频/1967787388695097345.json, 视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json, 视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json, 视频生成/文生视频/1950558909717204993.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1963965754733416450.json、视频生成/图生视频/1956634658516471809.json、视频生成/图生视频/1967787388695097345.json、视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json、视频生成/文生视频/wan2.2视频工作流_2013120474653401089.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `SaveVideo` —— 4/6 个有
- `VHS_VideoCombine` —— 4/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `FlashVSRNode` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `WanFunInpaintToVideo` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 12 | 6 | 48% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 36% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 12，6 个样本，取值分散，一致性仅 48%
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
