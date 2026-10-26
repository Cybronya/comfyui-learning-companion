---
name: unknown_workflow_video_lora_sampler_460
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5086
common_nodes: [AILab_QwenVL, CFGZeroStar, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PreviewAny, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVideoNAG]
problems: []
missing: []
members: [数字人/数字人/2025.1113终极生视频_许老师版_1988918533176299522.json, 视频生成/图生视频/Wan2.2 PainterI2V慢动作优化无限长视频生成(QwenVL增强)_1992287754939854849.json, 视频生成/图生视频/Wan2.2_14B_i2v_SVI2_2007636774910173185.json, 视频生成/图生视频/video_wan2_2_14B_i2v_painteri2v_1988481476389945345.json, 视频生成/图生视频/video_wan2_2_14B_i2v_svi2-painterI2V_1997917830655934465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_460

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（数字人/数字人/2025.1113终极生视频_许老师版_1988918533176299522.json、视频生成/图生视频/Wan2.2 PainterI2V慢动作优化无限长视频生成(QwenVL增强)_1992287754939854849.json、视频生成/图生视频/Wan2.2_14B_i2v_SVI2_2007636774910173185.json、视频生成/图生视频/video_wan2_2_14B_i2v_painteri2v_1988481476389945345.json、视频生成/图生视频/video_wan2_2_14B_i2v_svi2-painterI2V_1997917830655934465.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_QwenVL`
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `PainterI2V` —— 3/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `FlashVSRNode` —— 1/5 个有
- `ForLoopClose` —— 1/5 个有
- `ForLoopOpen` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `JWStringConcat` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | lcm | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
