---
name: unknown_workflow_video_lora_sampler_661
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.87725
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [平台全量/ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658.json, 视频生成/图生视频/Lightx2v+PainterI2V+Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜_1992227734485094401.json, 视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA-速度更快，效果更好-图生视频_1991087874728898561.json, 视频生成/图生视频/图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_661

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/ComfyUI-PainterI2V：Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜！_1990660150207942658.json、视频生成/图生视频/Lightx2v+PainterI2V+Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜_1992227734485094401.json、视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA-速度更快，效果更好-图生视频_1991087874728898561.json、视频生成/图生视频/图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `AddLabel` —— 2/4 个有
- `Float` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `Int` —— 2/4 个有
- `PainterI2V` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `easy int` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MuyeTextEditOutput` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 50% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 4 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
