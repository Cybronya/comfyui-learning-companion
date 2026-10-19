---
name: unknown_workflow_sampler_clip_vae
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.9738
common_nodes: [CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1951683752307142657.json, 视频生成/图生视频/1967787388695097345.json, 视频生成/图生视频/1967772488862150657.json, 视频生成/图生视频/1994764866990878721.json, 视频生成/图生视频/1950181163430273026.json, 视频生成/图生视频/2053650114769637377.json, 视频生成/图生视频/2054459129242103809.json, 视频生成/图生视频/2046114491431133185.json, 视频生成/图生视频/2066869280796405762.json, 视频生成/图生视频/1984131896915492865.json, 视频生成/图生视频/1973739180855529474.json, 视频生成/图生视频/1950374828178104322.json, 视频生成/文生视频/Wan2.2 AI视频生成加速工作流_1954053840410857473.json, 视频生成/文生视频/wan2.2+GGUF+light4步加速lora图生视频工作流_1995845028314505218.json, 视频生成/文生视频/1950558909717204993.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1951683752307142657.json、视频生成/图生视频/1967787388695097345.json、视频生成/图生视频/1967772488862150657.json、视频生成/图生视频/1994764866990878721.json、视频生成/图生视频/1950181163430273026.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 14/15 个有
- `LoraLoaderModelOnly` —— 13/15 个有
- `UNETLoader` —— 13/15 个有
- `PathchSageAttentionKJ` —— 7/15 个有
- `CFGZeroStar` —— 4/15 个有
- `UnetLoaderGGUF` —— 4/15 个有
- `CLIPLoaderGGUF` —— 1/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `LG_LoadImage` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `VHS_VideoCombine` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 15 | 60% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 15 | 43% |
| 采样算法 | 3.5 | 1 - 3.5 | 15 | 51% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，15 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，15 个样本，取值分散，一致性仅 43%
- 采样算法 中位数 3.5，观测区间 1 - 3.5，15 个样本
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
