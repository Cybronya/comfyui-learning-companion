---
name: unknown_workflow_sampler_unet_vae_16
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.854111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/360°环绕视角-子弹时间_2111145426987606018.json, 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图生视频-自动提示词_2084469087677276162.json, 视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466.json, 视频生成/图生视频/MiniMax H3 REF2VA开源版-全能参考生视频-自动提示词_2084469128441720833.json, 视频生成/图生视频/MiniMax H3 REF2VA开源版-全能参考生视频-自动提示词_2084926692421885953.json, 视频生成/图生视频/MiniMax H3 图生视频 首尾帧视频 加速版_2091148846310191105.json, 视频生成/图生视频/MiniMax H3 多图参考 音频参考 加速优化版_2091125673569112066.json, 视频生成/图生视频/MiniMax H3 多图参考 音频参考 加速版_2090781925186301953.json, 视频生成/图生视频/MiniMax H3 多图参考 音频参考 极速生视频 优化版_2090429442127646721.json, 视频生成/图生视频/MiniMax H3全能参考+首帧+参考音频_2093611760375910402.json, 视频生成/图生视频/MiniMax H3全能参考+首帧+参考音频（一次解决声音一致性和角色一致性）_2088866600530309121.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧视频_加速版_2109821309583708162.json, 视频生成/图生视频/MiniMax_H3_图生视频_首尾帧视频_加速版_2110559708200398849.json, 视频生成/图生视频/全能参考+首帧+音频｜MiniMax H3声音角色双一致_2108370045545041922.json, 视频生成/图生视频/加速版-MiniMax H3 图生视频 首尾帧视频_2091065912949567490.json, 视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json, 视频生成/文生视频/BF16 iniMax-H3文生视频、图生视频、多图全能参考、首尾帧+加速版合集全能工作流作流加速版_2084727508074852354.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_16

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/360°环绕视角-子弹时间_2111145426987606018.json、视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-图生视频-自动提示词_2084469087677276162.json、视频生成/图生视频/MiniMax H3 REF2VA-Lightx2v-官方4步加速lora-V0.1-全能参考生视频_2086095420035518466.json、视频生成/图生视频/MiniMax H3 REF2VA开源版-全能参考生视频-自动提示词_2084469128441720833.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/18 个有
- `EasyCache` —— 12/18 个有
- `SaveVideo` —— 12/18 个有
- `PrimitiveFloat` —— 11/18 个有
- `ImageResizeKJv2` —— 10/18 个有
- `MiniMaxH3ReferenceToVideo` —— 10/18 个有
- `PrimitiveStringMultiline` —— 10/18 个有
- `ResolutionSelector` —— 10/18 个有
- `VHS_VideoCombine` —— 10/18 个有
- `MiniMaxH3ImageToVideo` —— 9/18 个有
- `CR Prompt Text` —— 8/18 个有
- `Int` —— 8/18 个有
- `ShowAnything|Mie` —— 8/18 个有
- `LoadAudio` —— 7/18 个有
- `孤海注释` —— 7/18 个有
- `Fast Groups Bypasser (rgthree)` —— 5/18 个有
- `CM_IntToFloat` —— 4/18 个有
- `LoraLoaderModelOnly` —— 4/18 个有
- `ModelPatchTorchSettings` —— 4/18 个有
- `intToFloat _O` —— 3/18 个有
- `PreviewImage` —— 2/18 个有
- `CR Text` —— 1/18 个有
- `ImageCrop+` —— 1/18 个有
- `ImageScaleToTotalPixels` —— 1/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/18 个有
- `UniBlockSwap` —— 1/18 个有
- `忽略多组孤海` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
