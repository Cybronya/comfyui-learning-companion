---
name: unknown_workflow_video_lora_sampler_137
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.621
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Qwen-VL自动反推-图生视频-comfyui官方流-自用_1981244475731337218.json, 视频生成/图生视频/WAN2.2+Qwen3-VL 图片反推全自动 图生视频工作流_1982712132548599809.json, 视频生成/图生视频/WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_2038972688689008641.json, 视频生成/图生视频/WAN2.2图生视频_1999730211526766594.json, 视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json, 视频生成/图生视频/Wan2.2-LightX2V-I2V极致动态图生视频【高质量】_1981254959582928897.json, 视频生成/图生视频/Wan2.2_lightx2V_I2V图生视频fisher版_2001486989629288450.json, 视频生成/图生视频/Work-FIsh-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980300907424473089.json, 视频生成/图生视频/Work-Fisher_Qwen3VL-全自动图片反推+图生视频_1982359421470810113.json, 视频生成/图生视频/Work-Fisher_Qwen3VL-全自动首尾帧反推+图生视频_1982359410183946242.json, 视频生成/图生视频/fisher版Wan2.2_lightx2V_I2V_2001317113182777346.json, 视频生成/图生视频/wan2.2图生视频_2001269970967330818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_137

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Qwen-VL自动反推-图生视频-comfyui官方流-自用_1981244475731337218.json、视频生成/图生视频/WAN2.2+Qwen3-VL 图片反推全自动 图生视频工作流_1982712132548599809.json、视频生成/图生视频/WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_2038972688689008641.json、视频生成/图生视频/WAN2.2图生视频_1999730211526766594.json、视频生成/图生视频/WAN2.2图生视频终极版_2083953699881316354.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 11/12 个有
- `WanImageToVideo` —— 11/12 个有
- `easy cleanGpuUsed` —— 11/12 个有
- `RIFE VFI` —— 10/12 个有
- `Fast Groups Bypasser (rgthree)` —— 8/12 个有
- `wanBlockSwap` —— 8/12 个有
- `LoadImage` —— 7/12 个有
- `ImageLoader` —— 5/12 个有
- `Qwen3_VQA` —— 5/12 个有
- `easy showAnything` —— 5/12 个有
- `MultiplePathsInput` —— 4/12 个有
- `CR Text` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `easy seed` —— 2/12 个有
- `Any To Any` —— 1/12 个有
- `CompressImages` —— 1/12 个有
- `CreateVideo` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `VHS_SelectFilename` —— 1/12 个有
- `WanFirstLastFrameToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 12 | 100% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 100% |
| 重绘幅度 | normal | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 100%
- 重绘幅度 最常用 normal，12 个样本，一致性 100%
