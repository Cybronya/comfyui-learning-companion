---
name: unknown_workflow_video_lora_sampler_344
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.967833
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/FFGO官流-aiwood_1991601622407135233.json, 视频生成/图生视频/Wan2.2I2V_Native 图生视频工作流_1950193350159810562.json, 视频生成/图生视频/任意角色出现在任意场景_1989997752631349249.json, 视频生成/图生视频/多图合成视频_1990039527299444738.json, 视频生成/图生视频/🦖角色+场景=视频_2006187389928083458.json, 视频生成/文生视频/FFGO_激发Wan2.2多图参考潜能_1992972427164663810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_344

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/FFGO官流-aiwood_1991601622407135233.json、视频生成/图生视频/Wan2.2I2V_Native 图生视频工作流_1950193350159810562.json、视频生成/图生视频/任意角色出现在任意场景_1989997752631349249.json、视频生成/图生视频/多图合成视频_1990039527299444738.json、视频生成/图生视频/🦖角色+场景=视频_2006187389928083458.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 5/6 个有
- `ImageConcanate` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `SimpleMath+` —— 5/6 个有
- `easy imageRemBg` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `PathchSageAttentionKJ` —— 3/6 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/6 个有
- `WanImageToVideo` —— 3/6 个有
- `ImageSharpen` —— 2/6 个有
- `Compositor3` —— 1/6 个有
- `CompositorConfig3` —— 1/6 个有
- `ImageGetSize` —— 1/6 个有
- `InspyrenetRembg` —— 1/6 个有
- `LayerUtility: BooleanOperator` —— 1/6 个有
- `ResizeLongestToNode` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `Switch any [Crystools]` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6.5 | 5 - 8 | 6 | 77% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 50% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 5 - 8，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 50%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
