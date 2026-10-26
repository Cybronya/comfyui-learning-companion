---
name: unknown_workflow_video_lora_sampler_690
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.843667
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Lightx2v+PainterI2V+Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜_1992227734485094401.json, 视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA-速度更快，效果更好-图生视频_1991087874728898561.json, 视频生成/图生视频/图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_690

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Lightx2v+PainterI2V+Wan2.2图生视频增强节点，减少慢动作镜头+增强运镜_1992227734485094401.json、视频生成/图生视频/Wan2.2-Lightx2v-1108新版加速LoRA-速度更快，效果更好-图生视频_1991087874728898561.json、视频生成/图生视频/图生视频 Wan2.2 Lightx2v-I2V Moe模型，速度质量高性价比_1978318259030253569.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `Int` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `PainterI2V` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 8 | 3 | 65% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 8，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
