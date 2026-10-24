---
name: unknown_workflow_video_lora_sampler_418
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.9414
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 SVI2 Pro 10秒长视频_2036317087181840385.json, 视频生成/图生视频/Wan2.2-native-control-Inp_1955921227057647617.json, 视频生成/图生视频/smooth图生视频工作流_2067249517136797697.json, 视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json, 视频生成/图生视频/wan2.2极速4步图生视频_1963965754733416450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_418

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 SVI2 Pro 10秒长视频_2036317087181840385.json、视频生成/图生视频/Wan2.2-native-control-Inp_1955921227057647617.json、视频生成/图生视频/smooth图生视频工作流_2067249517136797697.json、视频生成/图生视频/wan2.2图生视频官方工作流_2037349147073843201.json、视频生成/图生视频/wan2.2极速4步图生视频_1963965754733416450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `WanImageToVideo` —— 3/5 个有
- `CreateVideo` —— 1/5 个有
- `FlashVSRNode` —— 1/5 个有
- `ImageBatchExtendWithOverlap` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `WanAdvancedI2V` —— 1/5 个有
- `WanFunInpaintToVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 5 | 33% |
| 采样算法 | 1 | 1 - 3.5 | 5 | 39% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 33%
- 采样算法 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
