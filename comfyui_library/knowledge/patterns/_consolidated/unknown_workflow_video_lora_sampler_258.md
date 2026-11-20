---
name: unknown_workflow_video_lora_sampler_258
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.633222
common_nodes: [CLIPLoader, CLIPTextEncode, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 官改图生视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958522667143950337.json, 视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json, 视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json, 视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json, 视频生成/图生视频/Work-FIsh-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980300907424473089.json, 视频生成/图生视频/fisher版Wan2.2_lightx2V_I2V_2001317113182777346.json, 视频生成/图生视频/提示词高度遵守，动态效果很好_1983516962250760194.json, 视频生成/图生视频/水墨风朗诵背景山水视频制作思路_2068956549908881410.json, 视频生成/图生视频/短剧制作-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1984186286053474306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_258

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 官改图生视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958522667143950337.json、视频生成/图生视频/Wan2.2 官改首尾帧视频（INP 模型 + GGUF Q8模型 + Lightx2V +KJ）_1958523149342162945.json、视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json、视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json、视频生成/图生视频/Work-FIsh-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980300907424473089.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 9 个 workflow 都包含：
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
- `WanImageToVideo` —— 8/9 个有
- `INTConstant` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 6/9 个有
- `wanBlockSwap` —— 5/9 个有
- `JWFloat` —— 2/9 个有
- `JWInteger` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `UnetLoaderGGUF` —— 2/9 个有
- `easy seed` —— 2/9 个有
- `CR Text` —— 1/9 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `WanFirstLastFrameToVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 56% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 9 | 100% |
| 采样算法 | 1 | 0 - 1 | 9 | 65% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | normal | - | 9 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 0 - 1，9 个样本
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 normal，9 个样本，一致性 78%
