---
name: unknown_workflow_video_lora_sampler_669
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, ImageBatchMulti, ImageFromBatch, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RepeatImageBatch, ResizeImagesByShorterEdge, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideoFFmpeg, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/MiniMax H3 小猫踏步舞专属流_2118273680668188673.json, 平台全量/MiniMax H3 视频人物替换_2117507945054429185.json, 平台全量/MiniMax H3汽车模型高铁转场_2120052668998705154.json, 平台全量/MiniMax H3视频主角替换_2119720542717693953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_669

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/MiniMax H3 小猫踏步舞专属流_2118273680668188673.json、平台全量/MiniMax H3 视频人物替换_2117507945054429185.json、平台全量/MiniMax H3汽车模型高铁转场_2120052668998705154.json、平台全量/MiniMax H3视频主角替换_2119720542717693953.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RepeatImageBatch`
- `ResizeImagesByShorterEdge`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `LoadVideo` —— 3/4 个有
- `MiniMaxH3PromptEnhancerT8` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `ShellAgentPluginOutputText` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
