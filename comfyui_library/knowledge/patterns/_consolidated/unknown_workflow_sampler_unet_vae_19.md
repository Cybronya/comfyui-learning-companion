---
name: unknown_workflow_sampler_unet_vae_19
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.732083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json, 视频生成/图生视频/MiniMax H3 无缝循环动态壁纸二次元风格live2d自动分辨率_2085541606505140226.json, 视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json, 视频生成/图生视频/MiniMax H3-全能参考-双图版_2089995459833192449.json, 视频生成/图生视频/MiniMax H3-全能参考-四图版_2094418452898476034.json, 视频生成/图生视频/MiniMax H3-全能参考一图版_2094433073793421313.json, 视频生成/图生视频/MiniMax H3：参考生视频_2095783894242127874.json, 视频生成/图生视频/MiniMax H3：图生视频_2095788026013249538.json, 视频生成/图生视频/MiniMax H3｜武打导演工作流 9组预设_2109867240077217794.json, 视频生成/图生视频/MiniMax H3｜武打导演工作流 9组预设_2113580846379786242.json, 视频生成/图生视频/MiniMax_H3_七套服装连续换装_2094786595428847617.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2102924951413153793.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2103672100170067969.json, 视频生成/图生视频/MiniMax_H3_参考生视频_2104844242353999874.json, 视频生成/图生视频/Minimax H3 9图参考_2114939074095173633.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 参考生视频_2108491242530234370.json, 视频生成/图生视频/Minimax H3 Veda 稀疏注意力8步极速版 首尾帧_2108488300557328386.json, 视频生成/图生视频/Minimax H3 参考图和参考视音频生成视频满血版_2105625287546462210.json, 视频生成/图生视频/Minimax H3 极速文戏 首尾贞工作流_2115253411544395777.json, 视频生成/图生视频/Minimax_H3_极速文戏_首尾贞工作流_2115945773815918594.json, 视频生成/图生视频/Minimax图生视频I2V_2099170083997315073.json, 视频生成/图生视频/Minimax多帧插入或者视频续写_2102590341739274241.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 FL2VA开源版-单图生成视频-工作流_2093578786934710274.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-尾帧视频-工作流_2093527771631931393.json、视频生成/图生视频/MiniMax H3 FL2VA开源版-首尾帧生成视频-工作流-v2版本_2092500053683433474.json、视频生成/图生视频/MiniMax H3 无缝循环动态壁纸二次元风格live2d自动分辨率_2085541606505140226.json、视频生成/图生视频/MiniMax H3-全能参考-三图版_2094413856083898369.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 23/24 个有
- `LoraLoaderModelOnly` —— 23/24 个有
- `PrimitiveBoolean` —— 23/24 个有
- `PrimitiveInt` —— 23/24 个有
- `VAEDecodeAudio` —— 23/24 个有
- `ResolutionSelector` —— 20/24 个有
- `PrimitiveStringMultiline` —— 18/24 个有
- `MiniMaxH3ReferenceToVideo` —— 15/24 个有
- `LoadAudio` —— 11/24 个有
- `MiniMaxH3ImageToVideo` —— 11/24 个有
- `GetImageSize` —— 6/24 个有
- `ImageScale` —— 4/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/24 个有
- `VedaSparseAttention` —— 4/24 个有
- `CR Text` —— 3/24 个有
- `ImageScaleToTotalPixels` —— 3/24 个有
- `AudioCrop` —— 2/24 个有
- `GetNode` —— 2/24 个有
- `GetVideoComponents` —— 2/24 个有
- `ImageFromBatch` —— 2/24 个有
- `LoadVideo` —— 2/24 个有
- `MinimaxH3LatentUpscaler3DRefineHandoff` —— 2/24 个有
- `SetNode` —— 2/24 个有
- `easy minimaxH3AudioLock` —— 2/24 个有
- `AudioConcat` —— 1/24 个有
- `ColorMatchV2` —— 1/24 个有
- `GetImageRangeFromBatch` —— 1/24 个有
- `INTConstant` —— 1/24 个有
- `Image Batch` —— 1/24 个有
- `ImageAddNoise` —— 1/24 个有
- `MiniMaxH3AddGuide` —— 1/24 个有
- `MiniMaxH3SigmaShift` —— 1/24 个有
- `TrimAudioDuration` —— 1/24 个有
- `VHS_LoadVideo` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
