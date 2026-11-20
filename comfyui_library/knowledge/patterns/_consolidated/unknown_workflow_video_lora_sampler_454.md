---
name: unknown_workflow_video_lora_sampler_454
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.622286
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 官改图生视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958522667143950337.json, 视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json, 视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json, 视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json, 视频生成/图生视频/Work-FIsh-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980300907424473089.json, 视频生成/图生视频/fisher版Wan2.2_lightx2V_I2V_2001317113182777346.json, 视频生成/文生视频/1022Alan测-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980811965771763713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_454

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 官改图生视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958522667143950337.json、视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json、视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json、视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json、视频生成/图生视频/Work-FIsh-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980300907424473089.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 6/7 个有
- `INTConstant` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `wanBlockSwap` —— 3/7 个有
- `JWFloat` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `UnetLoaderGGUF` —— 2/7 个有
- `easy seed` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 71% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 7 | 100% |
| 采样算法 | 1 | 0 - 1 | 7 | 59% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | normal | - | 7 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 71%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 0 - 1，7 个样本
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 normal，7 个样本，一致性 71%
