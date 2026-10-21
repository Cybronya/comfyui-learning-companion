---
name: unknown_workflow_sampler_clip_checkpoint_2
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.913937
common_nodes: [CFGGuider, CLIPTextEncode, EmptyFlux2LatentImage, RandomNoise, SamplerCustomAdvanced, SaveImage, T8LLaDAImageCheckpointLoader, T8LLaDAImageScheduler, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/AI一句话出二次元少女工作流_2099688939119534082.json, 图片生成/文生图/AI一句话出像素画工作流_2099689128639156225.json, 图片生成/文生图/AI一句话出图工作流_2099483718917382145.json, 图片生成/文生图/AI一句话出宠物写真工作流_2099673253303373825.json, 图片生成/文生图/AI一句话出服装模特图工作流_2099661996517056513.json, 图片生成/文生图/AI一句话出标志设计工作流_2099662212171390978.json, 图片生成/文生图/AI一句话出油画水彩工作流_2099689510945779714.json, 图片生成/文生图/AI一句话出竖版封面工作流_2099496937639727106.json, 图片生成/文生图/AI一句话出素描线稿工作流_2099689319828115458.json, 图片生成/文生图/AI一句话出角色立绘工作流_2099497044703531010.json, 图片生成/文生图/AI一句话出风景壁纸工作流_2099662102616166402.json, 图片生成/文生图/LLaDA-Image Base文生图·高保真图像生成_2097527015002955777.json, 图片生成/文生图/LLaDA-Image Turbo极速文生图·4步出图_2097527440242466817.json, 图片生成/文生图/LLaDA-Image-Turbo-4步-文生图_2098231001439887361.json, 图片生成/文生图/LLaDA-Image-文生图-全扩散架构_2098224508950896642.json, 图片生成/文生图/LLaDA-Image文字海报工作流_2099392086859673602.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/AI一句话出二次元少女工作流_2099688939119534082.json、图片生成/文生图/AI一句话出像素画工作流_2099689128639156225.json、图片生成/文生图/AI一句话出图工作流_2099483718917382145.json、图片生成/文生图/AI一句话出宠物写真工作流_2099673253303373825.json、图片生成/文生图/AI一句话出服装模特图工作流_2099661996517056513.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `T8LLaDAImageCheckpointLoader`
- `T8LLaDAImageScheduler`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 14/16 个有
- `CR Prompt Text` —— 12/16 个有
- `CLIPLoader` —— 11/16 个有
- `TextGenerate` —— 11/16 个有
- `PrimitiveInt` —— 2/16 个有
- `PrimitiveStringMultiline` —— 2/16 个有
- `T8SamplerLLaDAImageTurbo` —— 2/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
