---
name: unknown_workflow_video_lora_sampler_137
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.940667
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2003814653497122818.json, 视频生成/图生视频/2076115967696003073.json, 视频生成/图生视频/2075475746235174913.json, 视频生成/图生视频/2016945597965672449.json, 视频生成/图生视频/2027809490925527041.json, 视频生成/图生视频/2025568584335892482.json, 视频生成/图生视频/1955196269809602562.json, 视频生成/图生视频/2068892657300099074.json, 视频生成/图生视频/1949992607571206146.json, 视频生成/图生视频/1949874955704033281.json, 视频生成/图生视频/2056552561905332226.json, 视频生成/图生视频/2077340089688088578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_137

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2003814653497122818.json、视频生成/图生视频/2076115967696003073.json、视频生成/图生视频/2075475746235174913.json、视频生成/图生视频/2016945597965672449.json、视频生成/图生视频/2027809490925527041.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 11/12 个有
- `WanImageToVideo` —— 11/12 个有
- `LayerUtility: PurgeVRAM` —— 8/12 个有
- `PathchSageAttentionKJ` —— 8/12 个有
- `Int` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `ImageResize+` —— 3/12 个有
- `JWInteger` —— 3/12 个有
- `wanBlockSwap` —— 3/12 个有
- `ComfyMathExpression` —— 1/12 个有
- `DF_Int_to_Float` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `Text` —— 1/12 个有
- `UnetLoaderGGUF` —— 1/12 个有
- `WanFirstLastFrameToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 50% |
| Prompt 约束强度(CFG) | 7 | 4 - 14 | 12 | 58% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | lcm | - | 12 | 42% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 14，12 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，12 个样本，一致性 42%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
